import numpy as np
import cv2
from src.perspective import order_points
from src.quality import analyze_quality
from src.document_detector import find_document_corners
from src.config import Config

def test_order_points_shape():
    pts = np.array([[100, 100], [400, 100], [400, 600], [100, 600]], dtype=np.float32)
    ordered = order_points(pts)
    assert ordered.shape == (4, 2)
    assert np.allclose(ordered[0], [100, 100])

def test_quality_returns_expected_keys():
    image = np.full((300, 400, 3), 180, dtype=np.uint8)
    result = analyze_quality(image)
    assert "brightness_mean" in result
    assert "contrast_std" in result
    assert "blur_score" in result
    assert "skew_angle_degrees" in result

def test_document_detector_on_rectangle():
    image = np.zeros((500, 700, 3), dtype=np.uint8)
    cv2.rectangle(image, (100, 80), (600, 420), (255, 255, 255), 8)
    corners = find_document_corners(image, Config(min_contour_area_ratio=0.10))
    assert corners is not None
    assert len(corners) == 4

import cv2
import numpy as np
from .config import Config

def find_document_corners(image, config: Config):
    edges = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.GaussianBlur(edges, (5, 5), 0)
    edges = cv2.Canny(edges, config.canny_low, config.canny_high)

    contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image_area = image.shape[0] * image.shape[1]
    candidates = []

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < image_area * config.min_contour_area_ratio:
            continue
        perimeter = cv2.arcLength(contour, True)
        polygon = cv2.approxPolyDP(contour, config.approx_epsilon_ratio * perimeter, True)
        if len(polygon) == 4 and cv2.isContourConvex(polygon):
            candidates.append((area, polygon.reshape(4, 2)))

    if not candidates:
        return None

    candidates.sort(key=lambda item: item[0], reverse=True)
    return candidates[0][1].astype(np.float32)

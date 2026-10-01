import cv2
import numpy as np

def analyze_quality(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    brightness = float(np.mean(gray))
    contrast = float(np.std(gray))
    blur_score = float(cv2.Laplacian(gray, cv2.CV_64F).var())

    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=max(40, min(gray.shape) // 5))

    angles = []
    if lines is not None:
        for line in lines[:100]:
            theta = float(line[0][1])
            angle = np.degrees(theta) - 90.0
            while angle <= -45:
                angle += 90
            while angle > 45:
                angle -= 90
            angles.append(angle)

    skew = float(np.median(angles)) if angles else 0.0

    return {
        "brightness_mean": round(brightness, 3),
        "contrast_std": round(contrast, 3),
        "blur_score": round(blur_score, 3),
        "skew_angle_degrees": round(skew, 3),
    }

import cv2
from .config import Config

def resize_for_processing(image, config: Config):
    h, w = image.shape[:2]
    if w <= config.max_width:
        return image.copy(), 1.0
    scale = config.max_width / w
    resized = cv2.resize(image, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)
    return resized, scale

def edge_map(image, config: Config):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    return cv2.Canny(gray, config.canny_low, config.canny_high)

def make_threshold(image, config: Config):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 0)
    return cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, config.adaptive_block_size, config.adaptive_c
    )

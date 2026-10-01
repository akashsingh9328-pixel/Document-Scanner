from pathlib import Path
import cv2
import json

def load_image(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Input image not found: {p}")
    image = cv2.imread(str(p))
    if image is None:
        raise ValueError(f"OpenCV could not read the image: {p}")
    return image

def save_image(path: str, image):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not cv2.imwrite(str(p), image):
        raise IOError(f"Could not write image: {p}")

def save_json(path: str, data: dict):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, indent=2), encoding="utf-8")

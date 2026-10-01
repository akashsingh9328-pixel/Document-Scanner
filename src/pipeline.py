from pathlib import Path
from .config import Config
from .document_detector import find_document_corners
from .io_utils import load_image, save_image, save_json
from .perspective import four_point_transform
from .preprocessing import resize_for_processing, make_threshold
from .quality import analyze_quality

def run_pipeline(input_path: str, output_dir: str, config: Config | None = None):
    config = config or Config()
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    original = load_image(input_path)
    working, scale = resize_for_processing(original, config)

    corners = find_document_corners(working, config)

    if corners is not None and scale != 1.0:
        corners = corners / scale

    if corners is not None:
        scanned = four_point_transform(original, corners)
        detected = True
    else:
        scanned = original.copy()
        detected = False

    threshold = make_threshold(scanned, config)
    metrics = analyze_quality(scanned)
    report = {
        **metrics,
        "document_detected": detected,
        "input_file": str(input_path),
        "output_directory": str(output_dir),
        "original_width": int(original.shape[1]),
        "original_height": int(original.shape[0]),
        "output_width": int(scanned.shape[1]),
        "output_height": int(scanned.shape[0]),
    }

    save_image(output / "scanned_document.png", scanned)
    save_image(output / "threshold_document.png", threshold)
    save_json(output / "quality_report.json", report)
    return report

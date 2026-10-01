# Smart Document Scanner & Quality Analyzer

## 1. Overview
Smart Document Scanner & Quality Analyzer is a command-line Computer Vision project built with Python and OpenCV. It detects a document-like quadrilateral in an image, performs perspective correction, creates a clean scanned version, and reports image-quality measurements such as brightness, contrast, blur, and estimated skew.

The project is designed to be executable entirely from a terminal.

## 2. Features
- Document boundary detection using OpenCV edge and contour processing.
- Perspective transformation to produce a top-down scanned document.
- Automatic grayscale and adaptive-threshold preprocessing.
- Image-quality analysis:
  - brightness
  - contrast
  - blur estimate using Laplacian variance
  - estimated skew angle
- JSON quality report.
- Modular source code and validation tests.
- CLI interface with no GUI dependency.

## 3. Project Structure
```text
cv_document_scanner/
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── config.py
│   ├── io_utils.py
│   ├── preprocessing.py
│   ├── document_detector.py
│   ├── perspective.py
│   ├── quality.py
│   └── pipeline.py
├── tests/
│   └── test_core.py
├── data/
│   ├── input/
│   └── output/
├── docs/
│   └── diagrams/
├── statement.md
├── requirements.txt
└── README.md
```

## 4. Requirements
- Python 3.10+
- OpenCV
- NumPy
- Pillow
- PyTest

## 5. Installation
### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Linux/macOS
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 6. Run the project
Place an input image in `data/input/`, then run:

```bash
python -m src.cli --input data/input/document.jpg --output data/output
```

Or:

```bash
python src/cli.py --input data/input/document.jpg --output data/output
```

The command creates:
- `scanned_document.png`
- `threshold_document.png`
- `quality_report.json`

To print the quality report in the terminal:

```bash
python -m src.cli --input data/input/document.jpg --output data/output --print-report
```

## 7. Testing
Run:

```bash
pytest -q
```

## 8. Output interpretation
The JSON report contains:
- `brightness_mean`: average grayscale intensity.
- `contrast_std`: grayscale standard deviation.
- `blur_score`: variance of the Laplacian; lower values generally indicate stronger blur.
- `skew_angle_degrees`: estimated dominant text/document orientation.
- `document_detected`: whether a document-like quadrilateral was found.

These metrics are diagnostic indicators, not medical, legal, or production-quality guarantees.

## 9. Limitations
The detector works best when the document has a visible rectangular boundary, reasonable lighting, and sufficient contrast with the background. Highly cluttered backgrounds, severe shadows, folded pages, or strongly curved documents can reduce detection quality.

## 10. Future Enhancements
- Deep-learning document detection.
- Multi-page batch processing.
- OCR integration.
- Mobile deployment.
- Learned image-quality classification.

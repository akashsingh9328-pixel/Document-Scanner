# Project Statement

## Problem Statement
Photographs of documents often contain perspective distortion, uneven lighting, blur, and skew. These issues can make a document difficult to read or process automatically. The project addresses this problem by building a command-line Computer Vision pipeline that detects a document region, rectifies its perspective, improves its visual representation, and generates measurable quality indicators.

## Scope
The project covers single-image document detection, perspective correction, grayscale/threshold preprocessing, and basic quality analysis. It does not claim to replace a production document-management or OCR system.

## Target Users
- Students scanning notes and assignments.
- Users digitizing paper documents.
- Developers learning practical Computer Vision pipelines.
- Small teams needing a lightweight command-line preprocessing utility.

## High-Level Features
1. Detect document boundary.
2. Correct perspective.
3. Produce a clean thresholded scan.
4. Calculate image-quality metrics.
5. Save machine-readable JSON results.

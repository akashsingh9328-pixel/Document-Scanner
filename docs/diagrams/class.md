```mermaid
classDiagram
    class Config
    class CLI
    class Pipeline
    class DocumentDetector
    class Perspective
    class QualityAnalyzer
    class IOUtils
    class Preprocessing

    CLI --> Pipeline
    Pipeline --> Config
    Pipeline --> DocumentDetector
    Pipeline --> Perspective
    Pipeline --> QualityAnalyzer
    Pipeline --> IOUtils
    Pipeline --> Preprocessing
```

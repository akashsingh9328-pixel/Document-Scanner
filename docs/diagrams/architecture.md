```mermaid
flowchart LR
    CLI[Command Line Interface] --> PIPE[Pipeline]
    PIPE --> IO[Input/Output Utilities]
    PIPE --> PRE[Preprocessing]
    PIPE --> DET[Document Detector]
    PIPE --> PER[Perspective Transform]
    PIPE --> Q[Quality Analyzer]
    PIPE --> OUT[Output Files]
```

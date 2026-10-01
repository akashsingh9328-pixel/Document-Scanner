import argparse
import json
from .pipeline import run_pipeline

def build_parser():
    parser = argparse.ArgumentParser(
        description="Smart Document Scanner & Quality Analyzer"
    )
    parser.add_argument("--input", required=True, help="Path to input image")
    parser.add_argument("--output", default="data/output", help="Output directory")
    parser.add_argument("--print-report", action="store_true", help="Print JSON report")
    return parser

def main():
    args = build_parser().parse_args()
    try:
        report = run_pipeline(args.input, args.output)
        print("Processing completed successfully.")
        if args.print_report:
            print(json.dumps(report, indent=2))
    except Exception as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)

if __name__ == "__main__":
    main()

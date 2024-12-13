import sys
import json
from utils.header_checker import check_security_headers
from utils.report_writer import save_report

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <domain>")
        sys.exit(1)

    domain = sys.argv[1].strip()
    analysis_result = check_security_headers(domain)

    if "error" in analysis_result:
        print(f"Error analyzing domain {domain}: {analysis_result['error']}")
        sys.exit(1)

    report_paths = save_report(domain, analysis_result)

    print("Reports generated:")
    for format, path in report_paths.items():
        print(f"{format.upper()} report: {path}")
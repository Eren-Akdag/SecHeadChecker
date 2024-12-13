# Security Header Checker

A Python-based tool for analyzing and validating the security headers of websites. This tool helps developers and security professionals identify missing, misconfigured, or properly configured HTTP security headers to enhance website security.

---

## Features

- **Detailed Analysis**: Checks for the presence and configuration of critical HTTP security headers.
- **HSTS Validation**: Evaluates the `Strict-Transport-Security` header against best practices:
  - A minimum `max-age` of **31536000 seconds (1 year)**.
  - The presence of the `includeSubDomains` directive.
  - Support for the `preload` directive.
- **Report Generation**: Generates detailed reports in multiple formats (JSON, CSV, and human-readable table).
- **JSON, CSV, and Table Output**: Provides structured results for easy integration or reporting.

### Security Headers Checked

| **Header Name**             | **Description**                                                          |
|-----------------------------|--------------------------------------------------------------------------|
| `Content-Security-Policy`   | Defines approved sources of content.                                     |
| `Strict-Transport-Security` | Enforces secure (HTTP over SSL/TLS) connections to the server.           |
| `X-Content-Type-Options`    | Prevents MIME type sniffing.                                             |
| `X-Frame-Options`           | Controls whether the site can be framed.                                |
| `X-XSS-Protection`          | Enables cross-site scripting filters.                                   |
| `Referrer-Policy`           | Controls how much referrer information is included with requests.        |
| `Permissions-Policy`        | Manages browser features and APIs permissions.                          |

---

## Installation

### Prerequisites
- **Python 3.7+**
- **pip** (Python package manager)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/security-header-checker.git
   cd security-header-checker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the tool by providing the target domain as a command-line argument:

```bash
python3 main.py <domain>
```

### Example

```bash
python3 main.py example.com
```

**Sample Output**:
```json
{
    "domain": "https://example.com",
    "headers": [
        {
            "header": "Content-Security-Policy",
            "status": "Present",
            "details": "default-src 'self'; script-src 'none';"
        },
        {
            "header": "Strict-Transport-Security",
            "status": "Configured",
            "details": {
                "max-age": true,
                "includeSubDomains": true,
                "preload": false
            }
        },
        ...
    ]
}
```

---

## Project Structure

```
security-header-checker/
│
├── main.py                  # Entry point of the application
├── reports/                 # Folder to store the generated reports
├── utils/
│   ├── header_checker.py    # Core logic for security header analysis
│   ├── hsts_checker.py      # Validation logic for HSTS headers
│   ├── report_writer.py     # Logic for saving reports (JSON, CSV, Table)
│   └── status_code_checker.py # Logic for analyzing HTTP status codes
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## Dependencies

The project uses the following Python library:

- **requests**: Handles HTTP requests.

Install dependencies using:

```bash
pip install -r requirements.txt
```

### requirements.txt
```plaintext
requests
colorama
tabulate
prettytable
```

---

## How It Works

1. The tool sends an HTTP `GET` request to the target domain.
2. It retrieves the HTTP response headers.
3. Each header is analyzed for presence, correctness, and configuration:
   - If the header is missing, it is flagged as "Missing".
   - If present, additional checks are performed for specific headers (e.g., HSTS).
4. Outputs results in a structured JSON format.

---

## License

This project is licensed under the **MIT License**.

---
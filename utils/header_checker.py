import requests
from requests.exceptions import RequestException
from utils.hsts_checker import check_hsts
from utils.status_code_checker import analyze_status_code

SECURITY_HEADERS = {
    "Content-Security-Policy": "Defines approved sources of content.",
    "Strict-Transport-Security": "Enforces secure (HTTP over SSL/TLS) connections to the server.",
    "X-Content-Type-Options": "Prevents MIME type sniffing.",
    "X-Frame-Options": "Controls whether the site can be framed.",
    "X-XSS-Protection": "Enables cross-site scripting filters.",
    "Referrer-Policy": "Controls how much referrer information is included with requests.",
    "Permissions-Policy": "Manages browser features and APIs permissions."
}

def check_security_headers(domain):
    if not domain.startswith(('http://', 'https://')):
        domain = "https://" + domain

    try:
        response = requests.get(domain, timeout=10, verify=True)
    except RequestException as e:
        return {"domain": domain, "error": str(e)}

    # HTTP durum kodunu kontrol edin ve ekleyin
    status_code = response.status_code
    status_message = analyze_status_code(status_code)

    headers = response.headers
    results = {
        "domain": domain,
        "status_code": {"code": status_code, "message": status_message},
        "headers": []
    }

    for header in SECURITY_HEADERS:
        header_value = headers.get(header)
        if header_value:
            if header == "Strict-Transport-Security":
                hsts_results = check_hsts(header_value)
                status = "Configured" if all(hsts_results.values()) else "Misconfigured"
                details = hsts_results
            else:
                status = "Present"
                details = header_value
        else:
            status = "Missing"
            details = "N/A"

        results["headers"].append({
            "header": header,
            "status": status,
            "details": details
        })

    return results
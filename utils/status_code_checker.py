def analyze_status_code(status_code):
    if 100 <= status_code < 200:
        return "Informational: Request received, continuing process."
    elif status_code == 200:
        return "OK: The request has succeeded."
    elif status_code == 201:
        return "Created: The request has been fulfilled and a new resource is created."
    elif status_code == 202:
        return "Accepted: The request has been accepted for processing, but the processing is not complete."
    elif status_code == 204:
        return "No Content: The server successfully processed the request, but is not returning any content."
    elif status_code == 301:
        return "Moved Permanently: The resource has been permanently moved to a new URL."
    elif status_code == 302:
        return "Found: The resource is temporarily located at a different URL."
    elif status_code == 304:
        return "Not Modified: The resource has not been modified since the last request."
    elif 400 <= status_code < 500:
        if status_code == 400:
            return "Bad Request: The server could not understand the request."
        elif status_code == 401:
            return "Unauthorized: Authentication is required or has failed."
        elif status_code == 403:
            return "Forbidden: The server understands the request but refuses to authorize it."
        elif status_code == 404:
            return "Not Found: The server could not find the requested resource."
        elif status_code == 405:
            return "Method Not Allowed: The request method is not supported for the requested resource."
        elif status_code == 429:
            return "Too Many Requests: The user has sent too many requests in a given amount of time."
        else:
            return f"Client Error: {status_code}."
    elif 500 <= status_code < 600:
        if status_code == 500:
            return "Internal Server Error: The server encountered an unexpected condition."
        elif status_code == 501:
            return "Not Implemented: The server does not support the functionality required to fulfill the request."
        elif status_code == 502:
            return "Bad Gateway: The server received an invalid response from the upstream server."
        elif status_code == 503:
            return "Service Unavailable: The server is currently unavailable."
        elif status_code == 504:
            return "Gateway Timeout: The server did not receive a timely response from the upstream server."
        else:
            return f"Server Error: {status_code}."
    else:
        return f"Unknown Status Code: {status_code}"
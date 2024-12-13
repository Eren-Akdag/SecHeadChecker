def check_hsts(header_value):
    hsts_recommendations = {
        "max-age": 31536000,
        "includeSubDomains": True,
        "preload": True
    }

    directives = {}
    for item in header_value.split(';'):
        item = item.strip()
        if '=' in item:
            key, value = item.split('=', 1)
            directives[key.lower()] = value.strip()
        else:
            directives[item.lower()] = True

    results = {}
    max_age = directives.get("max-age")
    if max_age:
        try:
            results["max-age"] = int(max_age) >= hsts_recommendations["max-age"]
        except ValueError:
            results["max-age"] = False
    else:
        results["max-age"] = False

    results["includeSubDomains"] = directives.get("includesubdomains", False) is not False
    results["preload"] = directives.get("preload", False) is not False

    return results
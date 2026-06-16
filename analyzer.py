import requests as req

def safe_get(url):
    try:
        response = req.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0 (compatible; WebSecBot/1.0)"})
        return response
    except req.exceptions.RequestException:
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def check_headers(response):
    if not response:
        return {}
    headers = response.headers
    
    return headers

def normalize_url(url):
    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    return url

Security_Headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

def analyze_security_headers(response):
    headers = check_headers(response)
    results = {}
    
    for header in Security_Headers:
        results[header] = header in headers
    
    return results

def check_https(response):
    try:
        if not response:
            return False, None
        return response.url.startswith("https://"), response.status_code

    except Exception as e:
        print(f"An unexpected error occurred while checking HTTPS: {e}")
        return False, None

def check_robots(url):
    robots_url = url.rstrip("/") + "/robots.txt"
    response = safe_get(robots_url)
    if not response:
        return False, ""
    return response.status_code == 200 #, response.text if response.status_code == 200 else ""

def check_security_txt(url):
    security_txt_url = url.rstrip("/") + "/.well-known/security.txt"
    response = safe_get(security_txt_url)
    if not response:
        return False, ""
    return response.status_code == 200 #, response.text if response.status_code == 200 else ""

Common_Directories = [
    "admin",
    "login",
    "dashboard",
    "config",
    "backup",
    "test",
    "api",
    "uploads"
]

def scan_common_directories(url):
    found_directories = []
    
    for directory in Common_Directories:
        dir_url = url.rstrip("/") + "/" + directory
        response = safe_get(dir_url)
        if response and response.status_code == 200:
            found_directories.append(directory)
    
    return found_directories

def get_server_header(response):
    headers = check_headers(response)

    return headers.get("Server", "Unknown")

def check_redirects(response):

    if not response:
        return []

    return [r.url for r in response.history]

def generate_report(url):
    url = normalize_url(url)

    response = safe_get(url)
    if not response:
        return {
            "Error": "Unable to reach the URL. Please check the URL and try again."
        }
    
    headers = analyze_security_headers(response)
    https, https_status = check_https(response)
    robots_exists = check_robots(url)
    security_txt_exists = check_security_txt(url)
    common_dirs = scan_common_directories(url)
    server = get_server_header(response)
    redirects = check_redirects(response)

    report = {
        "URL": url,
        "Server": server,
        "Security Headers": headers,
        "HTTPS": https,
        "HTTP Status Code": https_status,
        "Robots.txt": robots_exists,
        "Security.txt": security_txt_exists,
        "Common Directories": common_dirs,
        "Redirects": redirects
    }

    return report

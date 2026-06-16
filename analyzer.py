import requests as req

def check_headers(url):
    response = req.get(url)
    headers = response.headers
    
    return headers

Security_Headers = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Referrer-Policy"
]

def analyze_security_headers(url):
    headers = check_headers(url)
    results = {}
    
    for header in Security_Headers:
        results[header] = header in headers
    
    return results

def check_https(url):
    return url.startswith("https://")

def check_robots(url):
    robots_url = url.rstrip("/") + "/robots.txt"
    response = req.get(robots_url)
    return response.status_code == 200, response.text if response.status_code == 200 else ""

def check_security_txt(url):
    security_txt_url = url.rstrip("/") + "/.well-known/security.txt"
    response = req.get(security_txt_url)
    return response.status_code == 200, response.text if response.status_code == 200 else ""

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
        response = req.get(dir_url)
        if response.status_code == 200:
            found_directories.append(directory)
    
    return found_directories

def generate_report(url):
    headers = analyze_security_headers(url)
    https = check_https(url)
    robots_exists, robots_content = check_robots(url)
    security_txt_exists, security_txt_content = check_security_txt(url)
    common_dirs = scan_common_directories(url)

    report = {
        "URL": url,
        "Security Headers": headers,
        "HTTPS": https,
        "Robots.txt": robots_exists,
        "Security.txt": security_txt_exists,
        "Common Directories": common_dirs
    }

    return report
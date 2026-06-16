# 🌐 WebSec - Web Security Analyzer

A lightweight Python-based Web Security Analysis Tool that helps identify basic security configurations of websites.

This project was built as part of my cybersecurity learning journey and demonstrates concepts such as HTTP requests, security headers, HTTPS verification, directory discovery, and web reconnaissance.

---

## 🚀 Features

### 🔒 Security Header Analysis

Checks for the presence of important security headers:

- Strict-Transport-Security (HSTS)
- Content-Security-Policy (CSP)
- X-Frame-Options
- X-Content-Type-Options
- Referrer-Policy


### 🌍 HTTPS Verification

- Detects whether the target website is using HTTPS
- Retrieves the HTTP status code


### 🤖 robots.txt Detection

Checks whether the website exposes a `robots.txt` file.

Example:

```
https://example.com/robots.txt
```


### 🛡️ security.txt Detection

Checks for the presence of a security disclosure file:

```
https://example.com/.well-known/security.txt
```


### 📂 Common Directory Discovery

Performs a safe check for commonly used directories:

- /admin
- /login
- /dashboard
- /config
- /backup
- /test
- /api
- /uploads


### 🖥️ Server Identification

Attempts to identify the web server from HTTP response headers.

Examples:

- Nginx
- Apache
- Cloudflare
- IIS



### 🔄 Redirect Detection

Detects HTTP redirects and displays the redirect chain.

Example:

```
http://example.com
    ↓
https://example.com
```

---

## 📸 Screenshots

### Main Program

<img width="375" height="287" alt="image" src="https://github.com/user-attachments/assets/12e63aa4-7110-434e-b94c-8412d2bbb036" />


### Example Analysis

<img width="377" height="592" alt="image" src="https://github.com/user-attachments/assets/bad7b6dd-8abc-4c99-9660-f9996902748b" />


---

## 🛠️ Technologies Used

- Python 3
- Requests Library

---

## 📦 Installation

- Install dependencies:
```bash
pip install requests
```

- Download the code:
[`main.py`](/main.py), [`analyzer.py`](/analyzer.py)

---

## ▶️ Usage

Run:

```bash
python main.py
```

Enter a website URL:

```text
github.com
```

or

```text
https://github.com
```

The tool automatically normalizes URLs and generates a security report.

---

## 📋 Example Output

```text
==================================================
          WebSec - Web Security Analyzer
==================================================
Enter the URL to analyze: github.com

--- Security Analysis Report ---

URL: https://github.com
Server: github.com

Security Headers:
  Strict-Transport-Security: Present
  Content-Security-Policy: Present
  X-Frame-Options: Present
  X-Content-Type-Options: Present
  Referrer-Policy: Present

HTTPS: Yes
HTTP Status Code: 200
Robots.txt: Found
Security.txt: Found

Common Directories Found:
  - login
  - dashboard
  - config
  - backup
  - test
  - uploads

No redirects found.

Do you want to analyze another URL? (y/n): 
```

---

## ⚠️ Disclaimer

This project is intended for educational and defensive security purposes only.

The tool performs passive analysis and does not exploit vulnerabilities, perform attacks, or bypass access controls.

Users are responsible for complying with all applicable laws and regulations when using this software.

---

## 🎯 Learning Objectives

This project helped me practice:

- Python programming
- HTTP requests and responses
- Security headers
- Web reconnaissance
- Exception handling
- Report generation
- Cybersecurity fundamentals

---

## 🙋‍♂️ Author - 

Kushagra Aggarwal

- Cyber Security Enthusiast
- Computer Science Student
- Alumnus, Dr. B.R. Ambedkar SoSE, Karol Bagh

<p style="margin: 0; padding: 0;">
  <span style="font-weight: bold; font-size: 1.1em;">Follow me on: </span>
  &nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/kushagraaggarwal639/"
     target="_blank"
     style="display: inline-flex; align-items: center; vertical-align: middle; text-decoration: none;">
    <img src="https://raw.githubusercontent.com/Kushagra639/Magasin_Connect/main/LinkedIn%20Logo.png"
         alt="LinkedIn"
         width="20"
         style="display: block;">
  </a>
  &nbsp;&nbsp;
  <a href="https://www.instagram.com/kushagraaggarwal639/"
     target="_blank"
     style="display: inline-flex; align-items: center; vertical-align: middle; text-decoration: none;">
    <img src="https://raw.githubusercontent.com/Kushagra639/Magasin_Connect/main/Instagram_logo.png"
         alt="Instagram"
         width="20"
         style="display: block;">
  </a>
</p>

---

## 📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.

---

Feel free to ⭐ the repository if you find it useful!

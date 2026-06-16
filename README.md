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

### 🖥️ Graphical User Interface

Built using CustomTkinter for a modern desktop experience.

Features include:

- URL input screen
- Scrollable analysis reports
- Error popups
- Theme switching
- Exportable reports
- Responsive interface

### 🌗 Theme Support

Supports:

- Light Mode
- Dark Mode
- Custom Pastel Theme

### 📄 Export Reports

Generate and export analysis reports directly to a text file.

Exported reports include:

- URL information
- Security headers
- HTTPS status
- HTTP status codes
- Server information
- Directory discovery results
- Redirect chains

---

## 📸 Screenshots

### Main Program

<img width="375" height="287" alt="image" src="https://github.com/user-attachments/assets/12e63aa4-7110-434e-b94c-8412d2bbb036" />


### Example Analysis

<img width="377" height="592" alt="image" src="https://github.com/user-attachments/assets/bad7b6dd-8abc-4c99-9660-f9996902748b" />

### Main Menu - GUI

<img width="1536" height="813" alt="image" src="https://github.com/user-attachments/assets/63fef802-40c2-4265-9aef-b1c7ad1d4d49" />
<img width="1536" height="816" alt="image" src="https://github.com/user-attachments/assets/be532ac1-0f9a-4a9f-ae01-9e0143573454" />


### Analyze Screen

<img width="1536" height="812" alt="image" src="https://github.com/user-attachments/assets/400f8cde-b884-4786-822e-68417f0012b9" />
<img width="1536" height="815" alt="image" src="https://github.com/user-attachments/assets/e783edbb-c99e-48bf-8d51-764281e2c043" />

### Loading Screen

<img width="1536" height="811" alt="image" src="https://github.com/user-attachments/assets/2396b4d6-6d9f-4400-bcd6-f49b2a2a239c" />

### Analysis Report Screen

<img width="1536" height="815" alt="image" src="https://github.com/user-attachments/assets/4c8858bd-09a6-49a1-ae1f-0b1b6d2ddb15" />
<img width="1536" height="817" alt="image" src="https://github.com/user-attachments/assets/ed8ed447-fdfb-416e-a156-67ea9aef74d7" />

### Exporting Analysis Report

<img width="397" height="176" alt="image" src="https://github.com/user-attachments/assets/2224447d-3620-44ba-9c87-da85ae1eb844" />


---

## 🛠️ Technologies Used

- Python 3
- Requests
- CustomTkinter
- Tkinter
- Pathlib
- DateTime

---

## 📦 Installation

### Install dependencies:
```bash
pip install requests customtkinter
```

### Download

*GUI Version*: (**Recommended**)
- [`main_gui.py`](/main_gui.py)
- [`analyzer.py`](/analyzer.py)
- [`pastel_theme.json`](/pastel_theme.json)

Alternatively, the *console version* can be used:

- [`main.py`](/main.py)
- [`analyzer.py`](/analyzer.py)

**Store all files in the same project folder; otherwise, you will have to change the path of all files in the code.**

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

## 📋 Example Output (Console Version)

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

- Python Programming
- HTTP Requests and Responses
- Security Headers
- Web Reconnaissance
- GUI Development
- Exception Handling
- Report Generation
- File Exporting
- User Experience Design
- Cybersecurity Fundamentals

---

## 🚧 Future Improvements

Planned future enhancements include:

- Multithreaded scanning
- JSON report export
- Additional security header checks
- SSL/TLS certificate analysis
- WHOIS lookup integration
- DNS information gathering
- Vulnerability intelligence integrations

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

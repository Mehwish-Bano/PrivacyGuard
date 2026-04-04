# 🔐 PrivacyGuard: Web Privacy Analyzer & Hardening Guide

This project is inspired by **CS50’s Introduction to Cybersecurity (Lecture 4: Preserving Privacy)**. It demonstrates how user data is exposed through HTTP headers, fingerprinting, and tracking technologies — and provides actionable steps to protect privacy.

---

## 🚀 Overview

Web privacy is often misunderstood. Even without logging in, websites can track you using:

- **HTTP Headers (User-Agent, Referer)**
- **Browser Fingerprinting**
- **Cookies (Session & Tracking)**
- **Tracking Parameters in URLs**
- **DNS Requests**

This project helps you **analyze and reduce your digital footprint**.

---

## 🛠️ Features

### 🔍 1. Privacy Analyzer (Python Script)
- Simulates a browser request  
- Displays exposed headers  
- Detects privacy risks automatically  

### 🛡️ 2. Hardening Checklist
- Step-by-step privacy protection guide  
- Covers browser, network, and system-level defenses  

---

## 💻 Technologies Used
- Python  
- Requests Library  

---

## ▶️ How to Run

```bash
git clone https://github.com/YOUR_USERNAME/PrivacyGuard.git
cd PrivacyGuard
pip install requests
python privacy_check.py

---

## 📸 Sample Output

--- PrivacyGuard: Advanced Analyzer ---

[!] Target URL: https://httpbin.org/get
[!] Your IP Address: xxx.xxx.xxx.xxx

[!] Exposed Headers:
    - User-Agent: Mozilla/5.0
    - Referer: https://www.google.com/search?q=privacy+test

⚠️ --- Privacy Risk Assessment ---
[Risk] Referer Header detected → Website knows your previous page!
[Risk] User-Agent exposed → Device fingerprinting possible!

✅ Analysis Complete!

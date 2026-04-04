import requests

def analyze_privacy():
    print("\n🔐 --- PrivacyGuard: Advanced Analyzer ---")

    url = input("\nEnter a URL to test (or press Enter for default): ")
    if not url:
        url = "https://httpbin.org/get"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Referer": "https://www.google.com/search?q=privacy+test"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        print(f"\n[!] Target URL: {url}")
        print(f"[!] Your IP Address: {data.get('origin', 'Unknown')}")

        print("\n[!] Exposed Headers:")
        for key, value in data['headers'].items():
            print(f"    - {key}: {value}")

        print("\n⚠️ --- Privacy Risk Assessment ---")

        if "Referer" in data['headers']:
            print("[Risk] Referer Header detected → Website knows your previous page!")

        if "User-Agent" in data['headers']:
            print("[Risk] User-Agent exposed → Device fingerprinting possible!")

        if "Origin" in data['headers']:
            print("[Risk] Origin header present → Request source identifiable!")

        print

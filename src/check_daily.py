import requests

url = "https://www.drikpanchang.com/tamil/tamil-month-panchangam.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, verify=False)
    print(f"Status: {response.status_code}")
    with open("debug.html", "w", encoding="utf-8") as f:
        f.write(response.text)
except Exception as e:
    print(f"Error: {e}")

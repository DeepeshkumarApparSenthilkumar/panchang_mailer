import requests

urls = [
    "https://www.drikpanchang.com/tamil/tamil-month-panchangam.html?geonameid=4887398",
    "https://www.drikpanchang.com/tamil/tamil-day-panchangam.html?geonameid=4887398",
    "https://www.drikpanchang.com/tamil/panchangam/tamil-panchangam.html?geonameid=4887398"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

for url in urls:
    try:
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        print(f"URL: {url} - Status: {response.status_code}")
    except Exception as e:
        print(f"URL: {url} - Error: {e}")

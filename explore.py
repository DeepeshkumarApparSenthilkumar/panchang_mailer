import requests
from bs4 import BeautifulSoup

url = "https://www.drikpanchang.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        text = link.get_text().strip()
        if 'tamil' in href.lower() or 'tamil' in text.lower():
            print(f"Text: {text} | Href: {href}")
            
except Exception as e:
    print(f"Error: {e}")

from bs4 import BeautifulSoup
import re

def parse_panchang(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    data = {}
    
    # Basic Info
    data['date'] = soup.find("h2", class_="dpPageShortTitle").get_text(strip=True) if soup.find("h2", class_="dpPageShortTitle") else "Unknown Date"
    data['location'] = "Chicago, IL"
    
    keys = soup.find_all("div", class_="dpTableKey")
    
    for key_div in keys:
        key_text = key_div.get_text(strip=True)
        
        value_div = key_div.find_next_sibling("div", class_="dpTableValue")
        
        if value_div:
            value_text = value_div.get_text(separator=" ", strip=True)
            # Remove info icon and other non-printable chars if necessary
            value_text = value_text.replace('\u24d8', '').strip()
            value_text = re.sub(r'\s+', ' ', value_text).strip()
            
            if key_text == "Sunrise":
                data['sunrise'] = value_text
            elif key_text == "Sunset":
                data['sunset'] = value_text
            elif key_text == "Moonrise":
                data['moonrise'] = value_text
            elif key_text == "Moonset":
                data['moonset'] = value_text
            elif key_text == "Tithi":
                data['tithi'] = value_text
            elif key_text == "Nakshathram":
                data['nakshatra'] = value_text
            elif key_text == "Yoga":
                data['yoga'] = value_text
            elif key_text == "Karana":
                data['karana'] = value_text
            elif key_text == "Rahu Kalam":
                data['rahu_kalam'] = value_text
            elif key_text == "Yamaganda":
                data['yamaganda'] = value_text
            elif key_text == "Gulikai":
                data['gulikai'] = value_text
            elif key_text == "Sunsign":
                data['sunsign'] = value_text
            elif key_text == "Moonsign":
                data['moonsign'] = value_text
            elif key_text == "Abhijit":
                data['abhijit_muhurta'] = value_text

    return data

if __name__ == "__main__":
    result = parse_panchang("daily_chicago_selenium.html")
    for k, v in result.items():
        try:
            print(f"{k}: {v}")
        except UnicodeEncodeError:
            print(f"{k}: {v.encode('ascii', 'ignore').decode('ascii')}")

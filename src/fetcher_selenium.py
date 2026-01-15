from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def fetch_chicago_html():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    # Suppress logs
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        print(f"Failed to initialize Chrome driver: {e}")
        return

    try:
        print("Navigating to Drik Panchang...")
        driver.get("https://www.drikpanchang.com/tamil/tamil-day-panchangam.html")
        
        # Wait for input
        print("Waiting for input box...")
        wait = WebDriverWait(driver, 20)
        input_box = wait.until(EC.presence_of_element_located((By.ID, "dp-direct-city-search")))
        
        print("Setting location to Chicago...")
        input_box.clear()
        input_box.send_keys("Chicago, IL, United States")
        time.sleep(2)
        input_box.send_keys(Keys.ENTER)
        
        # Wait for page reload/update
        # We can check if the location text changes
        print("Waiting for update...")
        time.sleep(10) # Simple wait for now
        
        # Save HTML
        with open("daily_chicago_selenium.html", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
            
        print("HTML saved to daily_chicago_selenium.html")
        
    except Exception as e:
        print(f"Error during execution: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    fetch_chicago_html()

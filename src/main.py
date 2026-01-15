import schedule
import time
import os
import sys
from fetcher_selenium import fetch_chicago_html
from parser import parse_panchang
from formatter import format_panchang_html
from mailer import send_email

# Configuration
HTML_FILE = "daily_chicago_selenium.html"
# User provided sender email
SENDER_EMAIL_DEFAULT = "dk5058203@gmail.com"
# Default TO_EMAIL to the sender for testing, or use env var
TO_EMAIL_ENV = os.environ.get("TO_EMAIL")
if not TO_EMAIL_ENV:
    TO_EMAIL_ENV = SENDER_EMAIL_DEFAULT
# Split by comma and strip whitespace to support multiple emails
TO_EMAIL = [email.strip() for email in TO_EMAIL_ENV.split(',')] if ',' in TO_EMAIL_ENV else TO_EMAIL_ENV

def job():
    print("Starting daily job...")
    
    # Ensure SENDER_EMAIL is set in env if not already
    if "SENDER_EMAIL" not in os.environ:
        os.environ["SENDER_EMAIL"] = SENDER_EMAIL_DEFAULT
        
    # Check for password
    if "SENDER_PASSWORD" not in os.environ:
        print("Error: SENDER_PASSWORD environment variable is not set.")
        print("Please set it using: $env:SENDER_PASSWORD='your_app_password'")
        return

    # 1. Fetch Data
    print("Fetching HTML...")
    fetch_chicago_html()
    
    # 2. Parse Data
    print("Parsing HTML...")
    if not os.path.exists(HTML_FILE):
        print(f"Error: {HTML_FILE} not found.")
        return
        
    try:
        data = parse_panchang(HTML_FILE)
    except Exception as e:
        print(f"Error parsing HTML: {e}")
        return
        
    # 3. Format Email
    print("Formatting email...")
    html_body = format_panchang_html(data)
    subject = f"Daily Panchangam for {data.get('date', 'Today')}"
    
    # 4. Send Email
    print(f"Sending email to {TO_EMAIL}...")
    send_email(subject, html_body, TO_EMAIL)
    print("Job completed.")

def run_scheduler():
    print("Scheduler started. Waiting for 06:00 AM...")
    schedule.every().day.at("06:00").do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--now":
        job()
    else:
        run_scheduler()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import datetime

def send_email(subject, body, to_email):
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PASSWORD")
    
    if not sender_email or not sender_password:
        print("Error: SENDER_EMAIL or SENDER_PASSWORD not set.")
        return

    msg = MIMEMultipart()
    msg['From'] = sender_email
    # Handle multiple recipients
    if isinstance(to_email, list):
        recipients = to_email
        msg['To'] = ", ".join(to_email)
    else:
        recipients = [to_email]
        msg['To'] = to_email

    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'html', 'utf-8'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        print(f"Sending email via SMTP to: {recipients}")
        server.sendmail(sender_email, recipients, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Test
    send_email("Test Subject", "<h1>Test Body</h1>", "test@example.com")

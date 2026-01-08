@echo off
:: Navigate to the project directory
cd /d "C:\Users\dk505\.gemini\antigravity\scratch\panchang_mailer"

:: Set environment variables
set SENDER_EMAIL=dk5058203@gmail.com
set SENDER_PASSWORD=zgag msod zihj brom

:: Run the script immediately (Task Scheduler will handle the timing)
python src/main.py --now

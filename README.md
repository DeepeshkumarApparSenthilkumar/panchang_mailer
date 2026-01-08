# Panchang Chicago Fetcher & Mailer

This project is an automated tool that fetches the daily Tamil Panchangam details for Chicago, IL from Drik Panchang and sends a beautifully formatted email with the details.

## Features

- **Automated Fetching**: Uses Selenium to navigate Drik Panchang and fetch the specific data for Chicago.
- **Data Parsing**: Extracts key details like Tithi, Nakshatra, Yoga, Rahu Kalam, Yamaganda, Sunrise, Sunset, etc.
- **Email Notification**: Formats the data into a clean HTML table and emails it to the subscriber.
- **Daily Schedule**: Configured to run automatically every day at 6:00 AM CST using GitHub Actions.

## Project Structure

- `src/main.py`: The entry point. Orchestrates fetching, parsing, formatting, and emailing.
- `src/fetcher_selenium.py`: Handles browser automation to get the correct HTML page for Chicago.
- `src/parser.py`: Parses the raw HTML to extract Panchangam data.
- `src/formatter.py`: Generates the HTML email body.
- `src/mailer.py`: Handles SMTP connection to send the email.
- `.github/workflows/daily_mailer.yml`: GitHub Actions configuration for daily automation.

## Setup & Usage

### Prerequisites

- Python 3.9+
- Google Chrome (for Selenium)
- A Gmail account with 2-Step Verification enabled and an App Password generated.

### Local Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd panchang_mailer
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Environment Variables:**
    You need to set the following environment variables for the mailer to work:
    - `SENDER_EMAIL`: Your Gmail address.
    - `SENDER_PASSWORD`: Your Google App Password (16 characters).
    - `TO_EMAIL`: The recipient's email address.

    **PowerShell Example:**
    ```powershell
    $env:SENDER_EMAIL='your_email@gmail.com'
    $env:SENDER_PASSWORD='your_app_password'
    $env:TO_EMAIL='recipient@example.com'
    ```

4.  **Run the script:**
    ```bash
    python src/main.py --now
    ```

### GitHub Actions (Automation)

This project is designed to run on GitHub Actions.

1.  Push the code to a GitHub repository.
2.  Go to **Settings > Secrets and variables > Actions**.
3.  Add the following **Repository Secrets**:
    - `SENDER_EMAIL`
    - `SENDER_PASSWORD`
    - `TO_EMAIL`
4.  The workflow is scheduled to run daily at 12:00 UTC (6:00 AM CST). You can also trigger it manually from the **Actions** tab.

## Dependencies

- `selenium`
- `webdriver-manager`
- `beautifulsoup4`
- `requests`
- `schedule`
- `lxml`

## License

[MIT](LICENSE)

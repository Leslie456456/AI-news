import os
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.fetch_news import NewsAggregator
from src.generate_briefing import BriefingGenerator


def send_email(subject, body):
    email_address = os.environ.get("EMAIL_ADDRESS")
    email_password = os.environ.get("EMAIL_APP_PASSWORD")

    if not email_address:
        raise ValueError("EMAIL_ADDRESS secret is missing.")
    if not email_password:
        raise ValueError("EMAIL_APP_PASSWORD secret is missing.")

    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = email_address
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(msg)

    print("Email sent successfully.")


def main():
    print("Fetching AI news...")
    aggregator = NewsAggregator()
    news = aggregator.fetch_all_news()

    print(f"Found {len(news)} relevant news items.")

    generator = BriefingGenerator(news)
    briefing = generator.generate_full_briefing()

    today = datetime.now().strftime("%Y-%m-%d")
    subject = f"Daily AI News Briefing - {today}"

    print("Sending email...")
    send_email(subject, briefing)

    print("Done.")


if __name__ == "__main__":
    main()

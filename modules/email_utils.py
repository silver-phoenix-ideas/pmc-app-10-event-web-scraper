import smtplib
import email
import ssl
import os
import modules.config as config


def prepare_email(sender: str, recipient: str, message: str) -> str:
    email_message = email.message.Message()
    email_message.add_header('from', f"{config.APP_TITLE} <{sender}>")
    email_message.add_header('to', recipient)
    email_message.add_header(
        'subject', f"[{config.APP_TITLE}] New Event Posted"
    )
    email_message.set_payload(message)

    return email_message.as_string()


def send_email(message: str) -> None:
    host = config.APP_EMAIL_HOST
    port = config.APP_EMAIL_PORT
    username = os.getenv("APP_EMAIL_USER")
    password = os.getenv("APP_EMAIL_PASS")
    context = ssl.create_default_context()
    sender = os.getenv("APP_EMAIL_INBOX")
    recipient = os.getenv("APP_EMAIL_INBOX")

    email_message = prepare_email(sender, recipient, message)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(sender, recipient, email_message)

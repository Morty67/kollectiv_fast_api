from email.mime.image import MIMEImage

from celery import Celery
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465


celery = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    broker_connection_retry_on_startup=True,
)


@celery.task
def send_email_message(image_bytes, recipient_email):
    try:
        # Create a MIMEMultipart object for an email
        msg = MIMEMultipart()
        msg["From"] = SMTP_USER
        msg[
            "To"
        ] = recipient_email  # Use the recipient address passed as an argument

        msg["Subject"] = "Optimized Image"

        # Add text content
        text = MIMEText("Optimized image is attached.")
        msg.attach(text)

        # Add an optimized image as an attachment
        img = MIMEImage(image_bytes, name="optimized_image.jpg")
        msg.attach(img)

        # Establish a connection and send an email
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.sendmail(SMTP_USER, msg["To"], msg.as_string())

    except Exception as e:
        print(f"Failed to send email: {str(e)}")

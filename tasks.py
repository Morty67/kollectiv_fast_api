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
    """
    Celery task to send an email with an optimized image attachment.

    Args:
        image_bytes (bytes): The optimized image content as bytes.
        recipient_email (str): The email address of the recipient.

    Returns:
        None

    Raises:
        Exception: If there is an error during the email sending process.

    Comments:
        - This task is designed to be used asynchronously with Celery.
            It takes the optimized image content in bytes and the
            recipient's email address as arguments.

        - The function creates a MIMEMultipart object for an email, attaches a
            text message, and adds the optimized image as an attachment.

        - It uses SMTP_SSL to establish a secure connection to the SMTP server
            and sends the email.

        - The function is decorated with @celery.task to make it a Celery task.

        - If any exception occurs during the email sending process,
            it is caught, and an error message is printed to the console.
            You may consider logging the error for better tracking.

    Usage:
        send_email_message.delay(optimized_image_bytes, "recipient@example.com")
    """
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

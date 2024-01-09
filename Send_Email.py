# import pre_installed libraries and packages

import os # used to interact with the operating system
import smtplib # used to send email using SMTP (simple mail transfer protocol)
from email.message import EmailMessage # importing EmailMessage class to use 'subject', 'from', 'to', 'cc' etc...
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

port = "use your ports"
Email_server = "test@outlook.com"

# load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir/".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
password_email = os.getenv("Password")





































# create email sender function taking all the email parameters same as our spreedsheet file

def sender_email(subject, receiver_email, name, due_date, invoice_no, amount):
    # Base text
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr((f"Email_sender, {sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        I hope you are well
        I just wanted to drop you a quick note to reminde you that {amount}£ in respect of our invoice
        {invoice_no} is due for payment on {due_date}.
        I would be really grateful if you could confirm that everything is on track for payment.
        Best regards
        Email_sender Name
        """
    )
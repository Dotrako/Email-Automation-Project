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

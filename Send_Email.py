# import pre_installed libraries and packages

import os # used to interact with the operating system
import smtplib # used to send email using SMTP (simple mail transfer protocol)
from email.message import EmailMessage # importing EmailMessage class to use 'subject', 'from', 'to', 'cc' etc...
from email.utils import formataddr
from pathlib import Path
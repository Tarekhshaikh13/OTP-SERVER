import smtplib
from email.mime.text import MIMEText
import os

sender = os.getenv('SMTP_EMAIL')

password = os.getenv('SMTP_APP_PASSWORD')


def send_otp_via_email(recipients,otp):

    msg = MIMEText(f"Your OTP code is {otp}")
    msg['Subject'] = "OTP Authentication"
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())

def send_success_via_email(recipients):
    msg = MIMEText(f"OTP Authenticated Successfully")
    msg['Subject'] = "OTP Authentication Successfull"
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())



import os
import random
from twilio.rest import Client

from fastapi import HTTPException

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')


twilio_client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# Helper function to generate OTP


# Helper function to send OTP via SMS using Twilio 
def send_otp_via_sms(phone_number: str, otp: str):
    try:
        message = twilio_client.messages.create(
            body=f"Your OTP code is {otp}",
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        return message.sid
    
    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Failed to send OTP : {e}")
    
def send_success_via_sms(phone_number: str):
    try:
        message = twilio_client.messages.create(
            body=f"OTP Authentication Successfull!",
            from_=TWILIO_PHONE_NUMBER,
            to=phone_number
        )
        return message.sid
    
    except Exception as e:

        raise HTTPException(status_code=500, detail=f"Failed Auth message: {e}")
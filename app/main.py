from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import redis
import random

from typing import Optional
import os
import logging
import logging_config
from sms_service import send_otp_via_sms,send_success_via_sms
from mail_service import send_otp_via_email,send_success_via_email

logging_config.setup_logging()

app = FastAPI()

# Initialize Redis client
redis_client = redis.Redis(host='redis', port=6379, password=os.getenv('REDIS_PASS'))

def generate_otp():
    return random.randint(100000, 999999)
# Define request model for OTP request
class OTPRequest(BaseModel):
    email : Optional[str] = None
    phone_number : Optional[str] = None
    otp: Optional[str] = None

@app.post("/send_otp/")
async def send_otp(request: OTPRequest):
    print(request)
    if not request.phone_number and not request.email:
        return {"status": 402, "message": "Either phone number or email is required"}

    otp = generate_otp()
    redis_key = f"otp:{request.phone_number or request.email}"

    try:
        # Store OTP in Redis with an expiration time (e.g., 5 minutes)
        success = redis_client.setex(redis_key, 300, otp)
        if not success:
            logging.error("Failed to store OTP in Redis")
            return {"status": 500, "message": "Internal server error"}

        responses = []

        if request.phone_number:
            try:
                send_otp_via_sms(request.phone_number, otp)
                
                responses.append(f"OTP sent to phone number {request.phone_number}")
            except Exception as e:
                logging.error(f"Failed to send OTP to phone number {request.phone_number}: {e}")
                responses.append(f"Failed to send OTP to phone number {request.phone_number}")

        if request.email:
            try:
                send_otp_via_email([request.email], otp)
                
                responses.append(f"OTP sent to email {request.email}")
            except Exception as e:
                logging.error(f"Failed to send OTP to email {request.email}: {e}")
                responses.append(f"Failed to send OTP to email {request.email}")

        logging.info(" ".join(responses))
        return {"status": 200, "message": " and ".join(responses)}

    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        return {"status": 500, "message": "Internal server error"}
    
    

# Endpoint to verify OTP
@app.post("/verify_otp/")
async def verify_otp(request : OTPRequest):
    redis_key = f"otp:{request.phone_number or request.email}"
    otp = request.otp
    # Retrieve OTP from Redis
    stored_otp = redis_client.get(redis_key)

    
    if stored_otp and stored_otp.decode('utf-8') == otp:
        try:
            if request.phone_number:
                send_success_via_sms(request.phone_number)
            if request.email:
                send_success_via_email([request.email])
        except Exception as e:
            logging.info(f"failed in sending success message, Exception : {e}")
        # OTP is correct, delete it from Redis
        redis_client.delete(redis_key)
        logging.info(f"OTP verified For {request.phone_number}")
        return {"message": "OTP verified successfully"}
    
    logging.info(f"OTP mismatch or expired for phone number: {request.phone_number}")
    raise HTTPException(status_code=400, detail="Invalid or expired OTP")

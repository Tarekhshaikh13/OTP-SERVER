# REDIS-FASTAPI OTP_SERVER

This FastAPI application provides endpoints to send and verify One-Time Passwords (OTPs). OTPs can be sent to either a phone number via SMS or an email address using SMTP. Redis is used for storing and managing OTPs with expiration.

## Features

- **Send OTP**: Send OTPs via SMS or Email
- **Verify OTP**: Verify OTPs against the stored value in Redis
- **Expiry Handling**: OTPs are automatically expired after a set period

## Prerequisites

- Docker (for containerization)
- Redis server (either locally or using Docker)
- Twilio (for sending SMS)
- An SMTP server for sending emails (Gmail used in the example)

## Setup

- add a .env file
- add proper mounts for logs and data folder
- add your keys and tokens

```env
# Twilio API credentials
TWILIO_ACCOUNT_SID=your_twilio_account_sid_here
TWILIO_AUTH_TOKEN=your_twilio_auth_token_here
TWILIO_PHONE_NUMBER=your_twilio_phone_number_here

# Redis server credentials
REDIS_PASS=your_redis_password_here

# Redis volume directories
REDIS_HOST_DIR=./redis_server/data
REDIS_CONTAINER_DIR=/data

# FastAPI logging directories
FASTAPI_LOG_HOST=./logs
FASTAPI_LOG_CONTAINER=/app/logs

# SMTP credentials
SMTP_EMAIL=your_smtp_email_here
SMTP_APP_PASSWORD=your_smtp_app_password_here


```bash
git clone https://github.com/Tarekhshaikh13/OTP-SERVER.git
cd OTP-SERVER
docker compose up -d





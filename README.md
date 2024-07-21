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


```bash
git clone https://github.com/Tarekhshaikh13/OTP-SERVER.git
cd OTP-SERVER
docker compose up -d



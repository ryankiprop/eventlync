# test_mpesa.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file in parent directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

from app.utils.mpesa import get_access_token, initiate_stk_push

print("🔍 Testing M-Pesa Configuration...")
print("=" * 50)

# Check environment variables
print("Environment variables:")
print(f"MPESA_ENV: {os.getenv('MPESA_ENV')}")
print(f"MPESA_CONSUMER_KEY: {'*' * len(os.getenv('MPESA_CONSUMER_KEY', ''))}")
print(f"MPESA_CONSUMER_SECRET: {'*' * len(os.getenv('MPESA_CONSUMER_SECRET', ''))}")
print(f"MPESA_SHORT_CODE: {os.getenv('MPESA_SHORT_CODE')}")
print(f"MPESA_PASSKEY: {'*' * 20}...")
print(f"MPESA_CALLBACK_URL: {os.getenv('MPESA_CALLBACK_URL')}")
print()

# Test 1: Access token
print("Test 1: Getting access token...")
try:
    token = get_access_token()
    print("✅ Access token successful:", token[:20] + "...")
except Exception as e:
    print("❌ Access token failed:", str(e))
    exit(1)

print()

# Test 2: STK Push
print("Test 2: Testing STK Push...")
try:
    resp = initiate_stk_push(
        phone_msisdn="254708374149",
        amount_kes=1,
        account_ref="test123",
        description="Test payment"
    )
    print("✅ STK Push successful!")
    print("Response:", resp)
except Exception as e:
    print("❌ STK Push failed:", str(e))

print()
print("🎯 If STK Push works, M-Pesa is configured correctly!")
print("🎯 If it fails, check your credentials in Safaricom Developer Portal.")

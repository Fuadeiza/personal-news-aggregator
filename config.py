from typing import List
import os
from dotenv import load_dotenv

load_dotenv()

CONFIG = {
    'base_url': "https://saharareporters.com",
    'openai_key': os.getenv("OPENAI_API_KEY"),
    'spitch_key': os.getenv("SPITCH_API_KEY"),
    'twilio_account_sid': os.getenv("TWILIO_ACCOUNT_SID"),
    'twilio_auth_token': os.getenv("TWILIO_AUTH_TOKEN"),
    'whatsapp_from': os.getenv("WHATSAPP_FROM_NUMBER"),
    'whatsapp_to': os.getenv("WHATSAPP_TO_NUMBER"),
    'gcs_bucket': os.getenv("GCS_BUCKET_NAME")
}
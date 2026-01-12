import os
from twilio.rest import Client

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

FROM_WHATSAPP = "whatsapp:+14155238886"
TO_WHATSAPP = os.getenv("TWILIO_TO_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_whatsapp_alert(message):
    client.messages.create(
        body=f"🚨 CYBER SECURITY ALERT 🚨\n\n{message}",
        from_=FROM_WHATSAPP,
        to=TO_WHATSAPP
    )

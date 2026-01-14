import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


COOLDOWN_SECONDS = 0
LAST_ALERT_FILE = "/tmp/last_telegram_alert.txt"

def can_send_alert():
    if not os.path.exists(LAST_ALERT_FILE):
        return True
    with open(LAST_ALERT_FILE, "r") as f:
        last_time = float(f.read())
    return (time.time() - last_time) > COOLDOWN_SECONDS

def update_last_alert_time():
    with open(LAST_ALERT_FILE, "w") as f:
        f.write(str(time.time()))

def send_telegram_alert(message):
    if not can_send_alert():
        return

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": f"🚨 CYBER SECURITY ALERT 🚨\n\n{message}"
    }

    requests.post(url, json=payload)
    update_last_alert_time()

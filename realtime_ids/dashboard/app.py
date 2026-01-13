from dotenv import load_dotenv
load_dotenv()

import os
import sys

# ✅ ADD PROJECT ROOT FIRST
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from flask import Flask, render_template


from ids.suricata_reader import get_suricata_alerts
from alerts.whatsapp_alert import send_whatsapp_alert
from anomaly_detection.detect_anomaly import run_anomaly_detection
from behavioral_analytics.behavior_model import run_ueba


app = Flask(__name__)

@app.route("/")
def index():
    anomaly_count = int(run_anomaly_detection())
    ueba_count = int(run_ueba())

    # Suricata alerts
    suricata_alerts = get_suricata_alerts()
    suricata_count = len(suricata_alerts)

    # Send WhatsApp alert if Suricata detects attack
    if suricata_count > 0:
        send_whatsapp_alert(suricata_alerts[0])

    anomaly_data = {
        "Normal": int(max(0, 100 - anomaly_count)),
        "Anomaly": int(anomaly_count)
    }

    ueba_data = {
        "Normal Users": int(max(0, 10 - ueba_count)),
        "Suspicious Users": int(ueba_count)
    }

    suricata_data = {
        "No Alerts": int(max(0, 20 - suricata_count)),
        "Suricata Alerts": int(suricata_count)
    }

    return render_template(
        "index.html",
        anomaly_count=anomaly_count,
        ueba_count=ueba_count,
        suricata_count=suricata_count,
        anomaly_data=anomaly_data,
        ueba_data=ueba_data,
        suricata_data=suricata_data,
        suricata_alerts=suricata_alerts
    )




if __name__ == "__main__":
    app.run(debug=True)

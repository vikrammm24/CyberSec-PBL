from dotenv import load_dotenv
load_dotenv()

import sys
import os
from flask import Flask, render_template

# add project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

from anomaly_detection.detect_anomaly import run_anomaly_detection
from behavioral_analytics.behavior_model import run_ueba

app = Flask(__name__)

@app.route("/")
def index():
    # Force Python int (NOT numpy.int64)
    anomaly_count = int(run_anomaly_detection())
    ueba_count = int(run_ueba())

    # Chart-safe data (all Python ints)
    anomaly_data = {
        "Normal": int(max(0, 100 - anomaly_count)),
        "Anomaly": int(anomaly_count)
    }

    ueba_data = {
        "Normal Users": int(max(0, 10 - ueba_count)),
        "Suspicious Users": int(ueba_count)
    }

    return render_template(
        "index.html",
        anomaly_count=anomaly_count,
        ueba_count=ueba_count,
        anomaly_data=anomaly_data,
        ueba_data=ueba_data
    )



if __name__ == "__main__":
    app.run(debug=True)

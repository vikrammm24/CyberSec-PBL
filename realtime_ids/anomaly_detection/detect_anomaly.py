import sys
import os
import pandas as pd
import joblib
from alerts.whatsapp_alert import send_whatsapp_alert

# ---------------- PATH SETUP ----------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

MODEL_PATH = os.path.join(PROJECT_ROOT, "anomaly_detection", "anomaly_model.pkl")
FEATURE_PATH = os.path.join(PROJECT_ROOT, "anomaly_detection", "feature_names.pkl")
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "UNSW_NB15_testing-set.csv")
RESULT_PATH = os.path.join(PROJECT_ROOT, "data", "anomaly_results.csv")

# ---------------- LOAD MODEL ----------------
model = joblib.load(MODEL_PATH)
feature_names = joblib.load(FEATURE_PATH)

# ---------------- DETECTION LOGIC ----------------
def run_anomaly_detection():
    data = pd.read_csv(DATA_PATH)

    X = data.drop(columns=['id', 'attack_cat', 'label'], errors='ignore')
    X = X.select_dtypes(include=['int64', 'float64'])
    X.fillna(0, inplace=True)

    X = X[feature_names]

    preds = model.predict(X)
    data["prediction"] = ["Normal" if p == 1 else "Anomaly" for p in preds]

    anomaly_count = (data["prediction"] == "Anomaly").sum()

    if anomaly_count > 0:
        send_whatsapp_alert(
            f"ML Anomaly Detection Alert!\nSuspicious flows detected: {anomaly_count}"
        )

    data.to_csv(RESULT_PATH, index=False)
    print(data["prediction"].value_counts())

    return anomaly_count


# ---------------- DIRECT RUN ----------------
if __name__ == "__main__":
    run_anomaly_detection()

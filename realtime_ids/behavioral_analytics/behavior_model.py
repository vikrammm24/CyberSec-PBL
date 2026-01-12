import sys
import os
import pandas as pd
from alerts.whatsapp_alert import send_whatsapp_alert

# ---------------- PATH SETUP ----------------
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)

DATA_PATH = os.path.join(PROJECT_ROOT, "behavioral_analytics", "user_logs.csv")
RESULT_PATH = os.path.join(PROJECT_ROOT, "data", "behavior_results.csv")

# ---------------- UEBA LOGIC ----------------
def behavior_analysis(row):
    reasons = []

    if row['login_hour'] < 6 or row['login_hour'] > 22:
        reasons.append("Abnormal login time")

    if row['connections'] > 25:
        reasons.append("Excessive connections")

    if row['bytes_sent'] > 50000:
        reasons.append("Unusual data transfer")

    if row['destination_port'] in [22, 3389]:
        reasons.append("Sensitive port access")

    if reasons:
        return "Suspicious", ", ".join(reasons)
    return "Normal", "None"


def run_ueba():
    df = pd.read_csv(DATA_PATH)

    df[['status', 'reason']] = df.apply(
        lambda row: pd.Series(behavior_analysis(row)), axis=1
    )

    suspicious_count = (df['status'] == "Suspicious").sum()

    if suspicious_count > 0:
        send_whatsapp_alert(
            f"UEBA Alert!\nSuspicious user activities detected: {suspicious_count}"
        )

    df.to_csv(RESULT_PATH, index=False)
    print(df[['user_id', 'status', 'reason']])

    return suspicious_count


# ---------------- DIRECT RUN ----------------
if __name__ == "__main__":
    run_ueba()

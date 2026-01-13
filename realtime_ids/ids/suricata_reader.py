import json

EVE_LOG = "/var/log/suricata/eve.json"

def get_suricata_alerts(limit=10):
    alerts = []
    try:
        with open(EVE_LOG, "r") as f:
            for line in reversed(list(f)):
                event = json.loads(line)
                if event.get("event_type") == "alert":
                    alert = event["alert"]["signature"]
                    src = event.get("src_ip", "unknown")
                    alerts.append(f"{alert} | Source: {src}")
                    if len(alerts) >= limit:
                        break
    except FileNotFoundError:
        pass

    return alerts

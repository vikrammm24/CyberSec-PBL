import subprocess
import re

def safe_ping(target):
    # Allow only domain names or IPs
    pattern = r"^[a-zA-Z0-9.-]+$"
    if not re.match(pattern, target):
        return "Invalid target"

    try:
        result = subprocess.run(
            ["ping", "-c", "3", target],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=5
        )
        return "Ping sent successfully"
    except Exception:
        return "Ping failed"

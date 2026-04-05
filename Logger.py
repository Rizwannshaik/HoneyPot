import json
from datetime import datetime

LOG_FILE = "logs.json"

def log_event(data):
    data["timestamp"] = datetime.now().isoformat()

    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    logs.append(data)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)
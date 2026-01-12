import json
from datetime import datetime

def log_event(event: dict):
    event["timestamp"] = datetime.utcnow().isoformat()
    print(json.dumps(event))


import json, os
from datetime import datetime, timezone, timedelta
from pathlib import Path

LOG = Path("logs/runs.json")
IST = timezone(timedelta(hours=5, minutes=30))

LOG.parent.mkdir(exist_ok=True)
runs = json.loads(LOG.read_text()) if LOG.exists() else []

now = datetime.now(timezone.utc)
repo = os.getenv("GITHUB_REPOSITORY", "local")
run_id = os.getenv("GITHUB_RUN_ID", "local")

runs.append({
    "time_utc": now.isoformat(timespec="seconds"),
    "time_ist": now.astimezone(IST).strftime("%Y-%m-%d %H:%M:%S"),
    "trigger": os.getenv("GITHUB_EVENT_NAME", "local"),
    "run_id": run_id,
    "run_url": f"https://github.com/{repo}/actions/runs/{run_id}",
})

LOG.write_text(json.dumps(runs[-200:], indent=2))
print("Logged run", run_id)

import json, re
from pathlib import Path

cron = json.loads(Path("config.json").read_text())["cron"]
wf = Path(".github/workflows/schedule.yml")
new = re.sub(r'(- cron: ")[^"]*(")', rf'\g<1>{cron}\g<2>', wf.read_text())
wf.write_text(new)
print(f"Schedule set to: {cron}")

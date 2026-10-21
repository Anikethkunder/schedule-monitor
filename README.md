# Schedule Monitor

Set a cron schedule, run a Python script on GitHub Actions, and view/prove the runs.

## Setup steps
1. Create a new GitHub repo (e.g. `schedule-monitor`). Leave it empty.
2. Upload ALL files from this folder (including the hidden `.github` folder), or use git:
   git init && git add . && git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/<username>/<repo>.git
   git push -u origin main
3. Repo -> Settings -> Actions -> General -> Workflow permissions -> select
   "Read and write permissions" -> Save.
4. Repo -> Settings -> Pages -> Source: "Deploy from a branch" -> Branch: main, folder / (root) -> Save.
5. Repo -> Actions -> "Scheduled run" -> Run workflow (manual test). A log entry appears in logs/runs.json.
6. Open https://<username>.github.io/<repo>/ to view the dashboard.

## Change the schedule
1. Edit config.json (cron is in UTC; IST = UTC + 5:30).
2. Run: python set_schedule.py
3. Commit and push.

Cron examples: "*/30 * * * *" every 30 min | "30 3 * * *" daily 9:00 AM IST | "0 */6 * * *" every 6 hours

## Proof it is scheduled
- Dashboard rows with trigger "schedule" were started by GitHub's cron.
- Each row links to the official Actions run page ("Triggered via schedule").
- Every run makes a commit by github-actions[bot].

# RedOps Orchestrator v2

API-first orchestrator for safe offensive security.

## Quickstart
```
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
cp .env.example .env
python run.py api
# new terminal
python run.py worker --queue nmap
curl -H "X-RedOps-Token: changeme" http://127.0.0.1:5000/health
```

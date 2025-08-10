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

## UI Development

```bash
cd webui
cp .env.example .env
npm install
npm run dev
# open http://127.0.0.1:5173
```

## Build & Serve via FastAPI

```bash
cd webui && npm run build
# restart the API; UI served at http://127.0.0.1:5000/ui
```

## Usage

```bash
# run worker for nmap queue
python run.py worker nmap
# start API
python run.py api --host 0.0.0.0 --port 5000
# UI: npm run dev (proxy) or build then access /ui
```

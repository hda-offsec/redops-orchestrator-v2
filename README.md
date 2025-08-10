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

## Web UI

Vue 3 interface built with Vite and Tailwind.

### Development
```bash
cd webui
npm install
npm run dev
# open http://127.0.0.1:5173
```
Environment variables:
- `VITE_API_BASE` (default `http://127.0.0.1:5000`)
- `VITE_DEFAULT_TOKEN` (default `changeme`)

### Build & Serve via FastAPI
```bash
cd webui && npm run build
# restart the API; UI served at http://127.0.0.1:5000/ui
```

### Manual test plan
1. Start backend workers and API:
   ```bash
   python run.py worker nmap
   python run.py api --host 0.0.0.0 --port 5000
   ```
2. In another terminal run `npm run dev` and browse to `http://127.0.0.1:5173`.
3. Submit an Nmap scan (`scanme.nmap.org`, profile `normal`) and observe toasts and results.
4. Build the UI (`npm run build`) and access it via `http://127.0.0.1:5000/ui`.

## Usage
```
# run worker for nmap queue
python run.py worker nmap
# start API
python run.py api --host 0.0.0.0 --port 5000
# UI: npm run dev (proxy) or build then access /ui
```

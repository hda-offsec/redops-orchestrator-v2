.PHONY: venv install run worker test lint up down

venv:
python3 -m venv .venv
. .venv/bin/activate && pip install -e .[dev]

run:
. .venv/bin/activate && python run.py api

worker:
. .venv/bin/activate && python run.py worker --queue nmap

test:
. .venv/bin/activate && PYTHONPATH=. pytest

lint:
. .venv/bin/activate && ruff check . && mypy .

up:
docker compose -f infra/docker-compose.yml up -d

down:
docker compose -f infra/docker-compose.yml down

once-nmap:
. .venv/bin/activate && python run.py once nmap --target localhost --profile normal

profiles-nmap:
. .venv/bin/activate && python run.py profiles nmap

health:
. .venv/bin/activate && python run.py health

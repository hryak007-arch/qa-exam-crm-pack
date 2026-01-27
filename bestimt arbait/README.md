# CRM minimal (for running QA pytest pack)

This is a minimal FastAPI + SQLite + SQLAlchemy project created to allow running the provided integration tests.

## Quick start (Windows / PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pytest -q
```

## Run API
```powershell
uvicorn app.main:app --reload
# open http://127.0.0.1:8000/docs
```

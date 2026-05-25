Collatz Sequence — Django App

Overview
- Small Django app that generates Collatz sequences, visualizes them, and stores history in SQLite.

Quick setup
1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # PowerShell
# or
.\.venv\Scripts\activate.bat   # cmd
```

2. Install dependencies:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

If `requirements.txt` is not present, install the essentials:

```powershell
.\.venv\Scripts\python.exe -m pip install django matplotlib djangorestframework django-cors-headers
```

Run the app

```powershell
cd App
..\.venv\Scripts\python.exe manage.py migrate
..\.venv\Scripts\python.exe manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

Main files
- App/backend/settings.py — Django settings
- App/api/views.py — API endpoints and views
- App/api/templates/api/collatz.html — Frontend UI
- App/db.sqlite3 — SQLite database (created after migrations)

API endpoints
- GET /api/collatz/?n=<number> — Generate sequence for `n` (returns sequence, steps, max_value, id)
- GET /api/history/ — Retrieve recent history (last 50 entries)
- GET /api/history/<id>/ — Retrieve one history entry
- DELETE /api/history/ — Clear all history entries

Troubleshooting
- If you see "ModuleNotFoundError" for packages, ensure the virtual environment is active and dependencies installed in that venv.
- If the server fails to start, check the terminal for missing packages and install them into `.venv`.

Development notes
- Database is SQLite at `App/db.sqlite3` by default.
- To reset history without the UI, run `python manage.py dbshell` or delete rows via Django shell:

```powershell
..\.venv\Scripts\python.exe manage.py shell
>>> from api.models import CollatzHistory
>>> CollatzHistory.objects.all().delete()
```

License
- No license specified. Add one if you plan to publish.

Contact
- For local development help, open an issue or ask for assistance.
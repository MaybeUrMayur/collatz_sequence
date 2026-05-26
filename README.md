# Collatz Conjecture Sequence Generator & Visualizer

A responsive, interactive web application and command-line utility built with Django, Chart.js, and Matplotlib. It allows users to generate and visualize Collatz sequences, view detailed analytics, and log history in an SQLite database.

---

## 🌌 Overview

The **Collatz Conjecture** (often referred to as the "3n + 1" problem) is a mathematical hypothesis: start with any positive integer $n$. If it is even, divide it by 2 ($n/2$); if it is odd, multiply it by 3 and add 1 ($3n + 1$). The conjecture asserts that no matter what value of $n$ you start with, the sequence will always eventually reach 1.

This project features:
* **Interactive Dark-Mode Dashboard**: A full-screen user interface where users can generate, view, and analyze sequences.
* **Dynamic Plotting**: Real-time charts rendered using [Chart.js](https://www.chartjs.org/) (for the web app) and [Matplotlib](https://matplotlib.org/) (for the CLI).
* **Database Tracking**: Persistent storage using SQLite to keep a detailed log of all computed sequences, including start numbers, step counts, peaks, and calculation timestamps.
* **REST API Endpoints**: Programmatic access to generate sequences and manage computation history.
* **Django Admin Integration**: Fully configured model search and filters for managing sequence histories.

---

## 📁 Repository Structure

The project code is organized as follows:

```text
collatz_sequence/
├── .venv/                  # Python virtual environment (optional/ignored)
├── App/                    # Main Django project directory
│   ├── api/                # Core application directory
│   │   ├── templates/      # HTML templates
│   │   │   └── api/
│   │   │       └── collatz.html   # Main full-width UI dashboard
│   │   ├── admin.py        # Django admin panel configuration
│   │   ├── apps.py         # Application configuration
│   │   ├── collatz_sequence.py # CLI entry point & sequence generator logic
│   │   ├── models.py       # CollatzHistory model schema
│   │   ├── urls.py         # Sub-app routing for endpoints
│   │   └── views.py        # API views and HTML rendering endpoints
│   ├── backend/            # Main Django configuration folder
│   │   ├── settings.py     # Database settings, apps registry, CORS configurations
│   │   ├── urls.py         # Root routing
│   │   └── wsgi.py / asgi.py
│   └── db.sqlite3          # SQLite Database storing history
└── README.md               # Project documentation
```

---

## 🛠️ Quick Start & Setup

Follow these steps to run the application on your local machine.

### 1. Prerequisites
Ensure you have **Python 3.10+** installed on your system.

### 2. Set Up a Virtual Environment (Recommended)
From the project root directory, run:

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On macOS / Linux / Git Bash:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
Install all the required python libraries using pip:
```bash
python -m pip install django matplotlib djangorestframework django-cors-headers
```

### 4. Database Setup & Migrations
Initialize the SQLite database schema by running Django migrations:
```bash
python App/manage.py migrate
```

---

## 🚀 Running the Application

This repository supports both a web interface and a terminal utility.

### Option A: The Web Dashboard (Django Server)
To run the web app, start the Django development server:
```bash
python App/manage.py runserver
```
Once started, open your web browser and navigate to:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

* **Interactive Controls**: Enter a starting number in the input box and click **Generate** (or press Enter) to visualize.
* **History Sidebar**: View recently generated sequences. Click any card in the history sidebar to load that sequence directly back into the chart.
* **Clear History**: Reset database logs directly from the sidebar.

### Option B: The Command Line Interface (CLI Plotter)
You can run the generator and plot a graph directly from your terminal using matplotlib:
```bash
python App/api/collatz_sequence.py
```
**Example execution flow:**
```text
--- The Collatz Conjecture Generator & Plotter ---
Enter a positive integer: 27

Collatz sequence for 27:
27 -> 82 -> 41 -> 124 -> 62 -> 31 -> 94 -> 47 -> ... -> 2 -> 1
Total steps taken: 111

Generating plot... (Close the plot window to finish the program)
```
*(A separate GUI window will open showing the sequence plot)*

---

## 🌐 API Reference

The web application exposes a set of REST endpoints:

### 1. Generate Sequence
* **Endpoint**: `GET /api/collatz/?n=<number>`
* **Description**: Computes the sequence, persists the data to the SQLite database, and returns statistics.
* **Query Parameters**:
  * `n` (integer, required): Starting number ($n > 0$)
* **Response Example (`GET /api/collatz/?n=6`)**:
  ```json
  {
    "sequence": [6, 3, 10, 5, 16, 8, 4, 2, 1],
    "steps": 8,
    "max_value": 16,
    "id": 14
  }
  ```

### 2. Get Sequence History
* **Endpoint**: `GET /api/history/`
* **Description**: Returns up to the last 50 calculations from the database (most recent first).
* **Response Example**:
  ```json
  {
    "history": [
      {
        "id": 14,
        "starting_number": 6,
        "total_steps": 8,
        "max_value": 16,
        "created_at": "2026-05-26T14:23:10.123456Z",
        "sequence": [6, 3, 10, 5, 16, 8, 4, 2, 1]
      }
    ],
    "count": 1
  }
  ```

### 3. Get Specific Calculation Details
* **Endpoint**: `GET /api/history/<id>/`
* **Description**: Retrieves details for a specific calculation record using its database ID.

### 4. Clear Calculation History
* **Endpoint**: `DELETE /api/history/`
* **Description**: Deletes all records from the `CollatzHistory` database table.

---

## 🔑 Administrative Settings

To view, inspect, or manage records in the admin dashboard:
1. Create a superuser:
   ```bash
   python App/manage.py createsuperuser
   ```
2. Navigate to **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)** and log in with your credentials.
3. You can search, filter, and view the list of generated sequences through the **Collatz Histories** model interface.
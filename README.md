# Personal Finance Dashboard & API

A professional financial management solution featuring a robust **FastAPI** backend and a **Power BI** interactive dashboard. This project follows clean code standards and SOLID principles.

## 🚀 Tech Stack

* **Backend:** Python 3.13+ with FastAPI
* **Architecture:** SOLID Principles (SRP, LSP, DIP)
* **Data Validation:** Pydantic Schemas & Decimal for monetary precision
* **Storage:** Local CSV Repository (Abstracted for easy database migration)
* **Frontend/BI:** Power BI Desktop & DAX
* **Environment:** Isolated via Virtual Environments (.venv)

## 📂 Project Structure

```text
├── data/               # Raw financial records (CSV format)
├── models/             # Domain logic (Transaction model)
├── repository/         # Data access layer (FinancialRepository)
├── routes/             # API Endpoints (FastAPI Routers)
├── schemas/            # Pydantic validation schemas
├── pbix/               # Power BI project files
├── main.py             # Application entry point
└── .venv/              # Isolated python environment
🛠️ Key Features
Financial Precision: Uses Decimal type to ensure two-decimal place accuracy in balances.

Automated Documentation: Swagger UI available at /docs for real-time testing.

Modular Design: Full separation between business logic, data storage, and web routes.

🏁 How to Run
Activate Environment:

Bash

source .venv/Scripts/activate
Start the API:

Bash

uvicorn main:app --reload
Check Documentation: Open http://127.0.0.1:8000/docs in your browser.

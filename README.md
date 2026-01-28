# 💰 Personal Finance Dashboard & API

A comprehensive financial management solution featuring a robust **FastAPI** backend and an interactive **Power BI** dashboard. This project is built using professional software engineering standards, including **SOLID** principles and strict data typing.

## 🚀 Tech Stack

* **Backend:** Python 3.13+ with FastAPI
* **Architecture:** SOLID Principles (SRP, LSP, DIP)
* **Data Validation:** Pydantic Schemas & Decimal for monetary precision
* **Storage:** CSV Repository (Abstracted for future SQL integration)
* **Frontend/BI:** Power BI Desktop & DAX

## 📂 Project Structure

```text
├── data/               # Raw financial records (CSV format)
├── models/             # Domain logic and business rules
├── repository/         # Data access layer (Persistence)
├── routes/             # API Endpoints (FastAPI Routers)
├── schemas/            # Pydantic validation and serialization
├── pbix/               # Power BI project files and resources
└── main.py             # Application entry point
🛠️ Key Features
Full CRUD: Create, Read, Update, and Delete financial transactions.

Financial Precision: Implemented with the Decimal type to avoid floating-point errors.

Automated Documentation: Interactive Swagger UI documentation available at /docs.

Modular Design: Clear separation between business logic, data storage, and web endpoints.

🏁 Getting Started
Activate Virtual Environment:

Bash

source .venv/Scripts/activate
Start the API:

Bash

uvicorn main:app --reload
Explore the API:
Access http://127.0.0.1:8000/docs to test endpoints.
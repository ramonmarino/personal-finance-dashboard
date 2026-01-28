# Personal Finance Dashboard & API

A comprehensive financial management solution that combines a robust **FastAPI** backend with a **Power BI** interactive dashboard. This project follows professional software engineering standards, including SOLID principles and automated documentation.

## 🚀 Tech Stack

* **Backend:** Python 3.13+ with FastAPI
* **Architecture:** SOLID Principles (SRP, LSP, DIP)
* **Data Validation:** Pydantic Schemas & Decimal for monetary precision
* **Storage:** Local CSV Repository (Abstracted for future SQL integration)
* **Frontend/BI:** Power BI Desktop & DAX
* **Environment:** Isolated with Virtual Environments (.venv)

## 📂 Project Structure

```text
├── data/               # Raw financial data (CSV format)
├── models/             # Domain models (Transaction class)
├── repository/         # Data access layer (FinancialRepository ABC)
├── routes/             # FastAPI routers and endpoints
├── schemas/            # Pydantic validation and serialization logic
├── service/            # Business logic and reporting (FinancialReporter)
├── pbix/               # Power BI project files and resources
├── main.py             # Application entry point and configuration
└── .venv/              # Project dependencies and environment
🛠️ Features
Financial Precision: Implemented using Decimal to avoid floating-point errors in balance calculations.

Automated Docs: Interactive API documentation (Swagger UI) available out-of-the-box.

Modular Routing: Clean separation between core logic and web endpoints.

Scalable Architecture: Easily swap CSV for a SQL database by extending the FinancialRepository.

🏁 Getting Started
Activate Virtual Environment:

Bash

source .venv/Scripts/activate
Run the Server:

Bash

uvicorn main:app --reload
Explore the API: Access http://127.0.0.1:8000/docs to test endpoints.

📊 Dashboard Overview (Power BI)
The API serves as the data provider for the Power BI dashboard, ensuring that visual insights are always based on validated and structured data.
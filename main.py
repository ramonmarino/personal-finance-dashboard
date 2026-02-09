from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.transaction import Transaction
from routes.financial import router as financial_router
from security.config import ALLOWED_ORIGINS
from db.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personal Finance API",
    description="API for tracking income and expenses following SOLID principles.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(financial_router, prefix="/api/v1")


@app.get("/")
def health_check() -> dict[str, str]:
    """Verify the operational status of the API.

    Provides a heartbeat endpoint to confirm that the server instance is
    active and responding to requests.

    Returns:
        dict[str, str]: A dictionary containing the online status and a
            personalized welcome message.
    """
    return {
        "status": "online",
        "message": "Welcome to the Personal Finance API, Ramon!",
    }

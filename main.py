from fastapi import FastAPI
from routes.financial import router as financial_router


app = FastAPI(
    title="Personal Finance API",
    description="API for tracking income and expenses following SOLID principles.",
    version="1.0.0",
)


app.include_router(financial_router, prefix="/api/v1")


@app.get("/")
def health_check():
    """Endpoint to verify if the API is online."""
    return {
        "status": "online",
        "message": "Welcome to the Personal Finance API, Ramon!",
    }

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware
from routes.financial import router as financial_router
from security.config import ALLOWED_ORIGINS

app = FastAPI(
    title="Personal Finance API",
    description="API for tracking income and expenses following SOLID principles.",
    version="1.0.0",
)

# CORS Middleware configuration to handle cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registering application routers
app.include_router(financial_router, prefix="/api/v1")


@app.get("/")
def health_check():
    """Verifies the operational status of the API.

    This heartbeat endpoint confirms the server is running and reachable.
    It serves as the primary check for monitoring tools.

    Returns:
        dict: A dictionary containing the API status and a
            welcome message for the user.
    """
    return {
        "status": "online",
        "message": "Welcome to the Personal Finance API, Ramon!",
    }

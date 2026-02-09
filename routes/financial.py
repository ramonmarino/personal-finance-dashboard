from decimal import Decimal
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from repository.financial_repository import SQLAlchemyRepository
from models.transaction import Transaction
from schema.transaction_shema import BalanceResponse, TransactionCreate

router = APIRouter()


@router.get("/balance", response_model=BalanceResponse)
def get_balance(db: Session = Depends(get_db)):
    """Retrieve the financial balance summary.

    Calculates the total income, total expenses, and the resulting current balance
    by fetching all transaction records from the repository and filtering by type.

    Args:
        db (Session): The SQLAlchemy database session provided by FastAPI dependency.

    Returns:
        dict: A dictionary containing the float values for total_income,
            total_expense, and current_balance.
    """
    repo = SQLAlchemyRepository(db)
    transactions = repo.get_all()

    total_income = sum(
        Decimal(str(t.amount)) for t in transactions if t.type == "income"
    )

    total_expense = sum(
        Decimal(str(t.amount)) for t in transactions if t.type == "expense"
    )

    return {
        "total_income": float(total_income),
        "total_expense": float(total_expense),
        "current_balance": float(total_income - total_expense),
    }


@router.post("/transactions", status_code=201)
def create_transaction(
    transaction_data: TransactionCreate, db: Session = Depends(get_db)
):
    """Register a new financial transaction.

    Processes the incoming transaction data, normalizes the transaction type
    to a standardized lowercase format, and persists the entity in the database.

    Args:
        transaction_data (TransactionCreate): The Pydantic schema containing
            transaction details like description, amount, type, and category.
        db (Session): The SQLAlchemy database session provided by FastAPI dependency.

    Returns:
        dict: A confirmation message indicating the successful registration.
    """
    repo = SQLAlchemyRepository(db)

    new_transaction = Transaction(
        category=transaction_data.category,
        description=transaction_data.description,
        type=transaction_data.transaction_type.lower().strip(),
        amount=float(transaction_data.amount),
    )

    repo.save(new_transaction)
    return {"message": "Transaction registered successfully in Database!"}

from fastapi import APIRouter,HTTPException
from service.reports import FinancialReporter
from repository.financial_repository import CSVRepository
from models.transaction import Transaction
from decimal import Decimal
from schema.transaction_shema import BalanceResponse, TransactionCreate


router = APIRouter()
repo = CSVRepository("data/financial_data.csv")

@router.get("/balance", response_model=BalanceResponse)
def get_balance():
    """Calculates and returns the total income and current balance.

    Returns:
        dict: A JSON object containing total_income and current_balance.
    """
    data = repo.get_all()
    total_income = sum(Decimal(row["Amount"]) for row in data if row["Type"] == "Income")
    total_expense = sum(
        Decimal(row["Amount"]) for row in data if row["Type"] == "Expense"
    )

    return {
        "total_income": total_income,
        "current_balance": total_income - total_expense,
    }


@router.post("/transactions", status_code=201)
def create_transaction(transaction_data: TransactionCreate):
    """Registers a new financial transaction in the CSV database.

    Args:
        transaction_data (TransactionCreate): Validated data from the request body.

    Returns:
        dict: A success message.
    """
    
    new_transaction = Transaction(
        category=transaction_data.category,
        description=transaction_data.description,
        transaction_type=transaction_data.transaction_type,
        amount=float(
            transaction_data.amount
        ),  
    )
    
    repo.save(new_transaction)

    return {"message": "Transaction registered successfully!"}

@router.put("/transactions/{index}")
def update_transaction(index: int, transaction_data: TransactionCreate):
    """Updates an existing transaction based on its list index."""

    updated_transaction = Transaction(
        category=transaction_data.category,
        description=transaction_data.description,
        transaction_type=transaction_data.transaction_type,
        amount=float(transaction_data.amount),
    )

    sucess = repo.update(index,updated_transaction)

    if not sucess:
        raise HTTPException(status_code=404, detail="Transaction index not found")
    
    return {"messagem": "Transaction uptaded sucessfully!"}

@router.delete("/transactions/{index}", status_code=204)
def delete_transaction(index:int):
    """Deletes an existing transaction based on its list index."""
    success = repo.delete(index)
    
    if not success:
        raise HTTPException(status_code=404, detail="Transaction index not found")
    
    return None 

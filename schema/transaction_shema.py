from pydantic import BaseModel, field_serializer
from decimal import Decimal


class BalanceResponse(BaseModel):
    """Schema for the balance endpoint response."""

    total_income: Decimal
    current_balance: Decimal

    @field_serializer("total_income", "current_balance")
    def serialize_decimal(self, v: Decimal):
        """Ensures two decimal places in the JSON response."""
        return f"{v:.2f}"




class TransactionCreate(BaseModel):
    """Schema for validating new transaction data from the client."""

    category: str
    description: str
    transaction_type: str  # 'Income' or 'Expense'
    amount: Decimal

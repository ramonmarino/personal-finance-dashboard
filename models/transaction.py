from sqlalchemy import Column, Integer, String, Float
from db.database import Base


class Transaction(Base):
    """Database model for financial transactions.

    Represents the schema for the 'transactions' table, storing details
    about income and expense entries.

    Attributes:
        id (int): Unique identifier and primary key for the transaction.
        description (str): A brief summary or name of the transaction.
        amount (float): The monetary value of the transaction.
        type (str): The classification of transaction (e.g., 'income', 'expense').
        category (str): The specific grouping for the transaction (e.g., 'food', 'salary').
    """

    __tablename__: str = "transactions"

    id: Column = Column(Integer, primary_key=True, index=True)
    description: Column = Column(String)
    amount: Column = Column(Float)
    type: Column = Column(String)
    category: Column = Column(String)

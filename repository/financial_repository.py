from abc import ABC, abstractmethod
from typing import List, Optional
from sqlalchemy.orm import Session
from models.transaction import Transaction


class FinancialRepository(ABC):
    @abstractmethod
    def save(self, transaction: Transaction) -> Transaction:
        pass

    @abstractmethod
    def get_all(self) -> List[Transaction]:
        pass

    @abstractmethod
    def delete(self, transaction_id: int) -> bool:
        pass


class SQLAlchemyRepository(FinancialRepository):
    def __init__(self, db: Session) -> None:
        """Initialize the repository with a database session.

        Args:
            db (Session): The SQLAlchemy database session.
        """
        self.db: Session = db

    def save(self, transaction: Transaction) -> Transaction:
        """Persist a transaction entity into the database.

        Args:
            transaction (Transaction): The transaction model instance to save.

        Returns:
            Transaction: The persisted transaction instance with updated metadata.
        """
        self.db.add(transaction)
        self.db.commit()
        self.db.refresh(transaction)
        return transaction

    def get_all(self) -> List[Transaction]:
        """Retrieve all transaction records from the database.

        Returns:
            List[Transaction]: A list of all transaction entities found.
        """
        return self.db.query(Transaction).all()

    def delete(self, transaction_id: int) -> bool:
        """Remove a transaction record by its unique identifier.

        Args:
            transaction_id (int): The primary key of the transaction to delete.

        Returns:
            bool: True if the transaction was found and deleted, False otherwise.
        """
        transaction: Optional[Transaction] = (
            self.db.query(Transaction).filter(Transaction.id == transaction_id).first()
        )
        if transaction:
            self.db.delete(transaction)
            self.db.commit()
            return True
        return False

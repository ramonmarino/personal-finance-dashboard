import csv
import os
from abc import ABC, abstractmethod
from models.transaction import (
    Transaction,
)  

class FinancialRepository(ABC):
    """Abstract base class for financial data storage."""

    @abstractmethod
    def save(self, transaction: Transaction):
        """Saves a single transaction to the storage."""
        pass

    @abstractmethod
    def get_all(self):
        """Retrieves all records from the storage."""
        pass


class CSVRepository(FinancialRepository):
    """CSV implementation of the financial repository."""

    def __init__(self, file_path: str):
        """Initializes the repository with a file path."""
        self.file_path = file_path

    def save(self, transaction: Transaction):
        """Appends a transaction to the CSV file without adding empty lines."""
        with open(self.file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(transaction.to_list())

    def get_all(self):
        """Reads all transactions from the CSV."""
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r", encoding="utf-8") as f:
            return list(csv.DictReader(line.strip() for line in f))

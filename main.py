import csv
import os

from datetime import datetime
from abc import ABC, abstractmethod


class Transaction:
    """Represents a single financial transaction."""

    def __init__(self, category, description, transaction_type, amount):
        self.date = datetime.now().strftime("%Y-%m-%d")
        self.category = category
        self.description = description
        self.transaction_type = transaction_type.capitalize()
        self.amount = amount

    def to_list(self):
        return [
            self.date,
            self.category,
            self.description,
            self.transaction_type,
            self.amount,
        ]


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
    """CSV implementation of the financial repository.

    Handles direct file system interactions with the CSV database.
    """
    def __init__(self,file_path: str):
        """Initializes the repository with a file path.

        Args:
            file_path (str): Path to the CSV file (e.g., 'data/financial_data.csv').
        """
        self.file_path = file_path

    def save(self,transaction: Transaction):
        """Appends a transaction to the CSV file without adding empty lines.

        Args:
            transaction (Transaction): The transaction object to be saved.
        """

        with open(self.file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(transaction.to_list())

    def get_all(self):
        """Reads all transactions from the CSV.

        Returns:
            list: A list of dictionaries representing each row in the CSV.
        """
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r", encoding="utf-8") as f:
            return list(csv.DictReader(line.strip() for line in f))

import csv
import os

from datetime import datetime
from abc import ABC, abstractmethod
from service.reports import FinancialReporter


class Transaction:
    """Represents a single financial movement."""

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


class FinanceRepository(ABC):
    """Abstract interface for financial data persistence."""

    @abstractmethod
    def save(self, transaction: Transaction):
        pass

    @abstractmethod
    def get_balance(self):
        pass


class CSVRepository(FinanceRepository):
    """Manages transaction saving and balance calculation in CSV."""

    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, transaction: Transaction):
        with open(self.file_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(transaction.to_list())

    def get_balance(self):
        """Calculates balance with extra robustness against spaces and case sensitivity."""
        total_income_fixed = 0.0
        total_expense = 0.0

        if not os.path.exists(self.file_path):
            return 0.0

        with open(self.file_path, "r", encoding="utf-8") as f:
            
            reader = csv.DictReader(line.strip() for line in f)

            for row in reader:
                try:
                    
                    amount_str = row.get("Amount") or row.get(" Amount")
                    type_str = row.get("Type") or row.get("Type")

                    if amount_str and type_str:
                        value = float(amount_str)
                        
                        if type_str.strip().capitalize() == "Income":
                            total_income_fixed += value
                        elif type_str.strip().capitalize() == "Expense":
                            total_expense += value
                except (ValueError, KeyError):
                    continue
        remaining_balance = total_income_fixed -total_expense        
        return total_income_fixed, remaining_balance


class ConsoleUI:
    """Handles user interaction via terminal."""

    @staticmethod
    def capture_transaction():
        print("\n--- New Financial Record ---")
        cat = input("Category: ")
        desc = input("Description: ")
        t_type = input("Type (Income/Expense): ")
        val = input("Amount: ")
        return Transaction(cat, desc, t_type, val)

    @staticmethod
    def show_menu():
        print("\n--- Financial Manager ---")
        print("1. Register New Transaction")
        print("2. View Current Balance")
        print("3. Exit")
        return input("Choose an option: ")


if __name__ == "__main__":
    repo = CSVRepository("data/financial_data.csv")
    
    reporter = FinancialReporter("data/financial_data.csv")

    while True:
        choice = ConsoleUI.show_menu()

        if choice == "1":
            new_tx = ConsoleUI.capture_transaction()
            try:
                repo.save(new_tx)
                print("\n✅ Saved!")
            except Exception as e:
                print(f"\n❌ Error: {e}")

        elif choice == "2":
            total_income_fixed, balance_remaining = repo.get_balance()
            
            print(f"\n💲 Income: {total_income_fixed:.2f}")
            print(f"💰 Current Balance: {balance_remaining:.2f}")
            
            reporter.display_detailed_extract()

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option!")

import csv
import os


class FinancialReporter:
    """Manages the generation of financial reports from CSV data.

    This class provides methods to process transaction data and present
    it in a readable format for the user.

    Attributes:
        file_path (str): The path to the CSV file containing financial records.
    """

    def __init__(self, file_path):
        """Initializes the FinancialReporter with a specific data file.

        Args:
            file_path (str): Path to the CSV file.
        """
        self.file_path = file_path

    def display_detailed_extract(self):
        """Reads the CSV and prints a formatted table of all expenses.

        It filters the records to show only those marked as 'Expense',
        displaying them in a structured table directly in the console.

        Returns:
            None: This method prints directly to the standard output.

        Notes:
            If the file specified in file_path does not exist, the method
            returns silently without printing.
        """
        if not os.path.exists(self.file_path):
            return

        print("\n" + "-" * 70)
        print(f"{'DATE':<12} | {'CATEGORY':<15} | {'DESCRIPTION':<25} | {'VALUE':>10}")
        print("-" * 70)

        with open(self.file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(line.strip() for line in f)

            for row in reader:
                if row.get("Type") == "Expense":
                    date = row.get("Date", "N/A")
                    cat = row.get("Category", "N/A")
                    desc = row.get("Description", "N/A")
                    val = float(row.get("Amount", 0))

                    print(f"{date:<12} | {cat:<15} | {desc:<25} | {val:>10.2f}")
        print("-" * 70)

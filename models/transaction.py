from datetime import datetime

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

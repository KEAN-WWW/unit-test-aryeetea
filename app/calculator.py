"""Calculator module providing basic arithmetic operations."""
class Calculator:
    """Simple calculator with basic arithmetic operations."""

    def add(self, a, b):
        """Return a + b."""
        return a + b

    def subtract(self, a, b):
        """Return a - b."""
        return a - b

    def multiply(self, a, b):
        """Return a * b."""
        return a * b

    def divide(self, a, b):
        """Return a / b. Raise ValueError on division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

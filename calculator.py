"""
A simple calculator module that performs basic arithmetic operations:
addition, subtraction, multiplication, and division.
"""


def add(a, b):
    """Return the sum of two integers."""
    return a + b


def subtract(a, b):
    """Return the difference of two integers (a - b)."""
    return a - b


def multiply(a, b):
    """Return the product of two integers."""
    return a * b


def divide(a, b):
    """Return the result of dividing a by b. Raise ValueError if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


class Calculator:
    """A simple calculator class that reuses the arithmetic functions."""

    def add(self, a, b):
        """Return the sum of two integers."""
        return add(a, b)

    def subtract(self, a, b):
        """Return the difference of two integers."""
        return subtract(a, b)

    def multiply(self, a, b):
        """Return the product of two integers."""
        return multiply(a, b)

    def divide(self, a, b):
        """Return the result of dividing a by b."""
        return divide(a, b)

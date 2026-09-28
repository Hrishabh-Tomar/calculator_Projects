"""
arithmetic.py
-------------
Basic arithmetic operations: add, subtract, multiply, divide,
percentage calculation, and a generic 'calculate' dispatcher.
"""

from .exceptions import InvalidOperationError


def _check_numbers(*values):
    """Internal helper: raise TypeError if any value isn't int/float."""
    for v in values:
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            raise TypeError(f"Expected a number, got {type(v).__name__}: {v!r}")


def add(a, b):
    _check_numbers(a, b)
    return a + b


def subtract(a, b):
    _check_numbers(a, b)
    return a - b


def multiply(a, b):
    _check_numbers(a, b)
    return a * b


def divide(a, b):
    _check_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def percentage(part, whole):
    """Return what percent 'part' is of 'whole'."""
    _check_numbers(part, whole)
    if whole == 0:
        raise ZeroDivisionError("Cannot calculate percentage with a whole of zero")
    return (part / whole) * 100


def calculate(a, b, operation):
    """
    Generic dispatcher: calculate(4, 2, 'add') -> 6
    """
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }

    if operation not in operations:
        raise InvalidOperationError(operation)

    return operations[operation](a, b)
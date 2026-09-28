"""
exceptions.py
-------------
Custom exceptions used across the calculator_tools package.
"""


class InvalidOperationError(Exception):
    """
    Raised when the caller asks for an operation that does not exist
    or is not supported (e.g. an unknown operator string like '%%',
    or an unsupported conversion type).
    """

    def __init__(self, operation, message=None):
        self.operation = operation
        if message is None:
            message = f"Unsupported or invalid operation: '{operation}'"
        super().__init__(message)
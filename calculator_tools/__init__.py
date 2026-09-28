"""
calculator_tools
-----------------
A small reusable Python PACKAGE (a folder with __init__.py, containing
several MODULES: arithmetic.py, statistics.py, converter.py, exceptions.py).
"""

from .arithmetic import add, subtract, multiply, divide, percentage, calculate
from .statistics import average, minimum, maximum, summarize
from .converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    convert_temperature,
    convert_length,
    convert_weight,
)
from .exceptions import InvalidOperationError

__all__ = [
    "add", "subtract", "multiply", "divide", "percentage", "calculate",
    "average", "minimum", "maximum", "summarize",
    "celsius_to_fahrenheit", "fahrenheit_to_celsius", "convert_temperature",
    "convert_length", "convert_weight",
    "InvalidOperationError",
]

__version__ = "1.0.0"
"""
statistics.py
--------------
Simple statistics helpers: average (mean), min, max.
"""

from .exceptions import InvalidOperationError


def average(numbers):
    """Return the average (mean) of a list/tuple of numbers."""
    if not isinstance(numbers, (list, tuple)):
        raise TypeError(f"Expected a list or tuple, got {type(numbers).__name__}")

    if len(numbers) == 0:
        raise ValueError("Cannot calculate average of an empty sequence")

    for n in numbers:
        if isinstance(n, bool) or not isinstance(n, (int, float)):
            raise TypeError(f"All items must be numbers, found: {n!r}")

    return sum(numbers) / len(numbers)


def minimum(numbers):
    if not numbers:
        raise ValueError("Cannot find minimum of an empty sequence")
    return min(numbers)


def maximum(numbers):
    if not numbers:
        raise ValueError("Cannot find maximum of an empty sequence")
    return max(numbers)


def summarize(numbers, stat="average"):
    """
    Generic dispatcher, mirrors arithmetic.calculate().
    summarize([1,2,3], 'average') -> 2.0
    """
    stats = {
        "average": average,
        "min": minimum,
        "max": maximum,
    }

    if stat not in stats:
        raise InvalidOperationError(stat)

    return stats[stat](numbers)
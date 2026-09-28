"""
converter.py
------------
Temperature conversion and simple unit conversion (length, weight).
"""

from .exceptions import InvalidOperationError


def _check_number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"Expected a number, got {type(value).__name__}: {value!r}")


# ---------- Temperature ----------

def celsius_to_fahrenheit(c):
    _check_number(c)
    return (c * 9 / 5) + 32


def fahrenheit_to_celsius(f):
    _check_number(f)
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c):
    _check_number(c)
    return c + 273.15


def convert_temperature(value, from_unit, to_unit):
    """
    convert_temperature(100, 'C', 'F') -> 212.0
    Supported units: 'C', 'F', 'K'
    """
    _check_number(value)
    if not isinstance(from_unit, str):
        raise TypeError(
            f"Expected from_unit to be a string, got {type(from_unit).__name__}: {from_unit!r}"
        )
    if not isinstance(to_unit, str):
        raise TypeError(
            f"Expected to_unit to be a string, got {type(to_unit).__name__}: {to_unit!r}"
        )

    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == to_unit:
        return value

    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        raise InvalidOperationError(from_unit, f"Unsupported temperature unit: '{from_unit}'")

    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius_to_fahrenheit(celsius)
    elif to_unit == "K":
        return celsius_to_kelvin(celsius)
    else:
        raise InvalidOperationError(to_unit, f"Unsupported temperature unit: '{to_unit}'")


# ---------- Simple unit conversion (length & weight) ----------

_LENGTH_TO_METERS = {
    "m": 1.0,
    "km": 1000.0,
    "cm": 0.01,
    "mm": 0.001,
    "mile": 1609.34,
    "ft": 0.3048,
}

_WEIGHT_TO_GRAMS = {
    "g": 1.0,
    "kg": 1000.0,
    "mg": 0.001,
    "lb": 453.592,
    "oz": 28.3495,
}


def convert_length(value, from_unit, to_unit):
    _check_number(value)
    if from_unit not in _LENGTH_TO_METERS:
        raise InvalidOperationError(from_unit, f"Unsupported length unit: '{from_unit}'")
    if to_unit not in _LENGTH_TO_METERS:
        raise InvalidOperationError(to_unit, f"Unsupported length unit: '{to_unit}'")

    meters = value * _LENGTH_TO_METERS[from_unit]
    return meters / _LENGTH_TO_METERS[to_unit]


def convert_weight(value, from_unit, to_unit):
    _check_number(value)
    if from_unit not in _WEIGHT_TO_GRAMS:
        raise InvalidOperationError(from_unit, f"Unsupported weight unit: '{from_unit}'")
    if to_unit not in _WEIGHT_TO_GRAMS:
        raise InvalidOperationError(to_unit, f"Unsupported weight unit: '{to_unit}'")

    grams = value * _WEIGHT_TO_GRAMS[from_unit]
    return grams / _WEIGHT_TO_GRAMS[to_unit]
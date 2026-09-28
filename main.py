"""
main.py
-------
Demonstrates the calculator_tools PACKAGE by IMPORTING it and calling
its FUNCTIONS, which live in different MODULES inside the package.
"""

import calculator_tools
from calculator_tools import arithmetic, statistics as calc_statistics, converter
from calculator_tools.exceptions import InvalidOperationError


def demo_arithmetic():
    print("\n--- Arithmetic ---")
    print("5 + 3 =", calculator_tools.add(5, 3))
    print("5 - 3 =", arithmetic.subtract(5, 3))
    print("5 * 3 =", calculator_tools.multiply(5, 3))
    print("6 / 3 =", calculator_tools.divide(6, 3))
    print("25 is what % of 200 ->", calculator_tools.percentage(25, 200), "%")
    print("calculate(10, 4, 'add') ->", calculator_tools.calculate(10, 4, "add"))


def demo_statistics():
    print("\n--- Statistics ---")
    scores = [80, 90, 70, 100, 60]
    print("scores:", scores)
    print("average ->", calculator_tools.average(scores))
    print("min ->", calculator_tools.minimum(scores))
    print("max ->", calculator_tools.maximum(scores))
    print("summarize(scores, 'average') ->", calc_statistics.summarize(scores, "average"))


def demo_converter():
    print("\n--- Temperature Conversion ---")
    print("100 C -> F:", calculator_tools.celsius_to_fahrenheit(100))
    print("32 F -> C:", calculator_tools.fahrenheit_to_celsius(32))
    print("25 C -> K:", calculator_tools.convert_temperature(25, "C", "K"))

    print("\n--- Unit Conversion ---")
    print("5 km -> m:", converter.convert_length(5, "km", "m"))
    print("10 lb -> kg:", converter.convert_weight(10, "lb", "kg"))


def demo_error_handling():
    print("\n--- Error Handling ---")

    try:
        calculator_tools.divide(10, 0)
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)

    try:
        calculator_tools.add(5, "abc")
    except TypeError as e:
        print("Caught TypeError:", e)

    try:
        calculator_tools.average([])
    except ValueError as e:
        print("Caught ValueError:", e)

    try:
        calculator_tools.calculate(5, 2, "modulus")
    except InvalidOperationError as e:
        print("Caught InvalidOperationError:", e)

    try:
        converter.convert_temperature(100, "C", "X")
    except InvalidOperationError as e:
        print("Caught InvalidOperationError:", e)


def main():
    print("=== calculator_tools package demo ===")
    demo_arithmetic()
    demo_statistics()
    demo_converter()
    demo_error_handling()
    print("\n=== Demo complete ===")


if __name__ == "__main__":
    main()
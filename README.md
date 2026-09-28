# Calculator Tools

A small, reusable Python package that demonstrates functions, modules, packages, and imports through a simple calculator toolkit — covering arithmetic, statistics, and unit conversion, with proper error handling.

## Features

- **Arithmetic** — add, subtract, multiply, divide, percentage calculation
- **Statistics** — average, minimum, maximum
- **Conversion** — temperature (Celsius/Fahrenheit/Kelvin), length, and weight
- **Custom exception handling** — including a custom `InvalidOperationError` for unsupported operations
- **Robust input validation** — handles division by zero, invalid data types, and unsupported operations gracefully

## Project Structure

calculator_tools_project/
├── calculator_tools/
│ ├── init.py # Package entry point — re-exports public functions
│ ├── arithmetic.py # add, subtract, multiply, divide, percentage, calculate()
│ ├── statistics.py # average, minimum, maximum, summarize()
│ ├── converter.py # temperature and unit (length/weight) conversion
│ └── exceptions.py # custom InvalidOperationError
├── main.py # Demo script — imports and exercises the package
└── README.md


## Requirements

- Python 3.7+
- No external dependencies (standard library only)

## Installation

Clone the repo and navigate into the project folder:

```bash
git clone https://github.com/<your-username>/python-projects.git
cd python-projects/calculator_tools_project
```

## Usage

Run the demo script from the project root:

```bash
python main.py
```

Or import the package in your own script:

```python
import calculator_tools

print(calculator_tools.add(5, 3))                        # 8
print(calculator_tools.percentage(25, 200))               # 12.5
print(calculator_tools.average([80, 90, 70, 100, 60]))    # 80.0
print(calculator_tools.convert_temperature(100, "C", "F")) # 212.0
```

## Error Handling

| Scenario | Exception Raised |
|---|---|
| Division by zero | `ZeroDivisionError` |
| Wrong data type (e.g. string instead of number) | `TypeError` |
| Empty list passed to statistics functions | `ValueError` |
| Unsupported operation or unit (e.g. `"modulus"`, unknown temp unit) | `InvalidOperationError` (custom) |

Example:

```python
from calculator_tools.exceptions import InvalidOperationError

try:
    calculator_tools.calculate(5, 2, "modulus")
except InvalidOperationError as e:
    print("Caught:", e)
```

## Key Concepts Demonstrated

- **Function** — a single reusable block of logic (e.g. `add(a, b)`)
- **Module** — a `.py` file grouping related functions (e.g. `arithmetic.py`)
- **Package** — a folder of modules tied together by `__init__.py` (`calculator_tools/`)
- **Import** — bringing package/module code into another file, shown in `main.py` via both `import calculator_tools` and `from calculator_tools import arithmetic`

## Author

Hrishabh Singh Tomar

## License

MIT

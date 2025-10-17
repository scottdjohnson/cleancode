# Simple Service

A simple educational example that demonstrates JSON processing in Python.

## Overview

This service takes a JSON string with `firstName`, `lastName`, and `city` fields and outputs those values to stdout.

## Project Structure

```
cleancode/
├── src/
│   └── simple_service/
│       ├── __init__.py
│       └── app.py           # Main application
├── tests/
│   ├── __init__.py
│   └── test_app.py          # Unit tests
├── .gitignore
└── README.md
```

## Installation

No installation required! Python 3.6+ is needed.

For running tests, install pytest:
```bash
pip install pytest
```

## Usage

Run the service from the project root directory:
```bash
PYTHONPATH=src python -m simple_service.app '{"firstName":"John","lastName":"Doe","city":"Seattle"}'
```

Output:
```
First Name: John
Last Name: Doe
City: Seattle
```

## Running Tests

```bash
# Run all tests
PYTHONPATH=src pytest tests/

# Run with verbose output
PYTHONPATH=src pytest -v tests/

# Run specific test file
PYTHONPATH=src pytest tests/test_app.py
```

## Development

The core logic is in `src/simple_service/app.py` with testable functions:
- `process_json_input()`: Parses JSON and extracts fields
- `format_output()`: Formats data for display
- `main()`: Handles command-line interaction and error handling

The package uses the `src/` layout, which is a Python packaging best practice that:
- Prevents accidental imports from the source directory
- Ensures tests run against the installed package
- Provides better isolation between source and test code


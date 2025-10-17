# Simple Service

A simple educational example that demonstrates JSON processing in Python.

## Overview

This service takes a JSON string with `firstName`, `lastName`, and `city` fields and outputs those values to stdout.

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
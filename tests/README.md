# Transend Python Client Tests

This directory contains tests for the Transend Python client.

## Test Structure

- `test_base_api.py`: Tests for the base API functionality
- `test_product_api.py`: Tests for the Product API endpoints
- `test_vehicle_api.py`: Tests for the Vehicle API endpoints
- `test_account_api.py`: Tests for the Account API endpoints
- `test_transend_client.py`: Tests for the main TransendAPIClient class

## Running Tests

### Using pytest

You can run all tests with pytest:

```bash
# From the project root directory
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test file:

```bash
pytest tests/test_base_api.py
```

Run a specific test class:

```bash
pytest tests/test_base_api.py::TestBaseAPI
```

Run a specific test method:

```bash
pytest tests/test_base_api.py::TestBaseAPI::test_init
```

### Using unittest

You can also run tests with unittest:

```bash
# From the project root directory
python -m unittest discover tests
```

Run a specific test file:

```bash
python -m unittest tests/test_base_api.py
```

## Coverage

To run tests with coverage:

1. Install coverage package:

```bash
pip install coverage
```

2. Run tests with coverage:

```bash
coverage run -m pytest
```

3. Generate coverage report:

```bash
coverage report
```

4. Generate HTML coverage report:

```bash
coverage html
```

Then open `htmlcov/index.html` in your browser to view the detailed report.

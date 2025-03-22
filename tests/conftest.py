"""
Pytest configuration file for Transend Python client tests.
This file contains shared fixtures and configurations for tests.
"""
import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_response():
    """
    Create a mock response object that mimics a requests.Response object.
    """
    mock = MagicMock()
    mock.json.return_value = {"data": "test_data"}
    mock.status_code = 200
    return mock


@pytest.fixture
def api_credentials():
    """
    Return test API credentials.
    """
    return {
        "api_key": "test_api_key",
        "api_token": "test_api_token",
        "base_url": "https://api.test.com"
    }

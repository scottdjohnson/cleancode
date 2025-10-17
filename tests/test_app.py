"""
Unit tests for the simple_service.app module.
"""
import json
import pytest
from simple_service.app import format_output


def test_format_output():
    """Test formatting output."""
    json_string = '{"firstName":"John","lastName":"Doe","city":"Seattle"}'
    result = format_output(json_string)
    expected = 'First Name: John\nLast Name: Doe\nCity: Seattle'
    assert result == expected


def test_format_output_invalid_json():
    """Test that invalid JSON raises JSONDecodeError."""
    with pytest.raises(json.JSONDecodeError):
        format_output('not valid json')



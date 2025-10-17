"""
Unit tests for the simple_service.app module.
"""
import json
import pytest
from simple_service.app import process_json_input, format_output


class TestProcessJsonInput:
    """Tests for process_json_input function."""
    
    @pytest.mark.parametrize("json_string,expected", [
        (
            '{"firstName":"John","lastName":"Doe","city":"Seattle"}',
            {'firstName': 'John', 'lastName': 'Doe', 'city': 'Seattle'}
        ),
        (
            '{"firstName":"Jane","lastName":"Smith","city":"Portland"}',
            {'firstName': 'Jane', 'lastName': 'Smith', 'city': 'Portland'}
        ),
        (
            '{"firstName":"","lastName":"","city":""}',
            {'firstName': '', 'lastName': '', 'city': ''}
        ),
        (
            '{}',
            {'firstName': '', 'lastName': '', 'city': ''}
        ),
        (
            '{"firstName":"Alice","extra":"ignored"}',
            {'firstName': 'Alice', 'lastName': '', 'city': ''}
        ),
    ])
    def test_process_json_input_valid(self, json_string, expected):
        """Test processing valid JSON input with various data."""
        result = process_json_input(json_string)
        assert result == expected
    
    def test_process_json_input_invalid_json(self):
        """Test that invalid JSON raises JSONDecodeError."""
        with pytest.raises(json.JSONDecodeError):
            process_json_input('not valid json')
    
    def test_process_json_input_empty_string(self):
        """Test that empty string raises JSONDecodeError."""
        with pytest.raises(json.JSONDecodeError):
            process_json_input('')


class TestFormatOutput:
    """Tests for format_output function."""
    
    @pytest.mark.parametrize("input_data,expected_output", [
        (
            {'firstName': 'John', 'lastName': 'Doe', 'city': 'Seattle'},
            'First Name: John\nLast Name: Doe\nCity: Seattle'
        ),
        (
            {'firstName': 'Jane', 'lastName': 'Smith', 'city': 'Portland'},
            'First Name: Jane\nLast Name: Smith\nCity: Portland'
        ),
        (
            {'firstName': '', 'lastName': '', 'city': ''},
            'First Name: \nLast Name: \nCity: '
        ),
    ])
    def test_format_output(self, input_data, expected_output):
        """Test formatting output with various input data."""
        result = format_output(input_data)
        assert result == expected_output



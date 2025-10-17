#!/usr/bin/env python3
"""
Main entry point for the simple service.
"""
import sys
import json


def process_json_input(json_string):
    data = json.loads(json_string)
    
    return {
        'firstName': data.get('firstName', ''),
        'lastName': data.get('lastName', ''),
        'city': data.get('city', '')
    }


def format_output(data):
    lines = [
        f"First Name: {data['firstName']}",
        f"Last Name: {data['lastName']}",
        f"City: {data['city']}"
    ]
    return '\n'.join(lines)


def main():
    json_string = sys.argv[1]
    data = process_json_input(json_string)
    output = format_output(data)
    print(output)


if __name__ == "__main__":
    main()

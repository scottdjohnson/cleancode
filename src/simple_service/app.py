#!/usr/bin/env python3
"""
Main entry point for the simple service.
"""
import sys
import json


def format_output(json_string):
    data = json.loads(json_string)
    
    lines = [
        f"First Name: {data.get('firstName', '')}",
        f"Last Name: {data.get('lastName', '')}",
        f"City: {data.get('city', '')}"
    ]
    return '\n'.join(lines)


def main():
    json_string = sys.argv[1]
    output = format_output(json_string)
    print(output)


if __name__ == "__main__":
    main()

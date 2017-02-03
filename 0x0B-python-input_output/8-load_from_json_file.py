#!/usr/bin/python3
import json
"""
Create an Object from a "JSON file".
"""


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.loads(f.read())

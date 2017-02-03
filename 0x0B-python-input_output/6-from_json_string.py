#!/usr/bin/python3
import json
"""
Return an object (Python data structure) represented by a JSON string.
"""


def from_json_string(my_str):
    return json.loads(my_str)

#!/usr/bin/python3
import json
from io import StringIO


def from_json_string(my_str):
    return json.load(StringIO(my_str))

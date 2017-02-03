#!/usr/bin/python3
import json
from io import StringIO

def load_from_json_file(filemame):
    with open(filemame, 'r') as f:
        json.load(StringIO(f.read()))

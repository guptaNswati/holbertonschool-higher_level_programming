#!/usr/bin/python3
import sys
import json
from io import StringIO
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
arg = sys.argv[1:]
save_to_json_file(arg,"add_item.json")
load_from_json_file("add_item.json")

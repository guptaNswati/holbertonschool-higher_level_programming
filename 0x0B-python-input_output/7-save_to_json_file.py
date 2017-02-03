#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filemame):
    with open(filemame, 'w') as f:
        f.write(json.dumps(my_obj, sort_keys=True))

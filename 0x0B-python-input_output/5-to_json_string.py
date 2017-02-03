#!/usr/bin/pyhton3
import json


def to_json_string(my_obj):
    return json.dumps(my_obj, sort_keys=True)

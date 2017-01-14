#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as e:
        res = None
        sys.stderr.write("Exception: %s\n" % e)
    return res

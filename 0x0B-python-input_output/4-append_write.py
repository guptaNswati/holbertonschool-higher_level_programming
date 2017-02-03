#!/usr/bin/python3
"""
Append a string at the end of a text file (UTF8) and return added number.
"""


def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        return f.write(text)

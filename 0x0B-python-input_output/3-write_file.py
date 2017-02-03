#!/usr/bin/python3
"""
Write a string to a text file (UTF8) and return the number of characters.
"""


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        return f.write(text)

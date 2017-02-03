#!/usr/bin/python3
"""
Read a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        print(f.read(), end="")

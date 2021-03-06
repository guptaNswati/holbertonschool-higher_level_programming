#!/usr/bin/python3
"""
This is the "say_my_name" module.

The say_my_name module supplies a simple function that prints a string literal.
"""


def say_my_name(first_name, last_name=""):
    """Print string literal.
    """
    if not (isinstance(first_name, str) or first_name):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str) or last_name):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}". format(first_name, last_name))

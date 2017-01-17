#!/usr/bin/python3
"""
This is the Print Name module.

The PrintName module supplies a simple function that prints a string literal.
For example,
>>> say_my_name("Holberton", "School"
My name is Holberton School
"""


def say_my_name(first_name, last_name=""):
    """Print string literal.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("first_name and last_name must be strings")
    print("My name is {:s} {:s}". format(first_name, last_name))

#!/usr/bin/python3
"""
This is the "text_indentation" module.

The "text-indentation" module provides a simple function text_indentation()
that prints a text with 2 new lines after each characters: ., ? and :.
"""


def text_indentation(text):
    """Print a text with 2 new lines after each characters: ., ? and :.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in line:
        if not (i == '.' or i == '?' or i == ':'):
            print("{:s}".format(i), end="")
        else:
            print("{:s}\n".format(i))

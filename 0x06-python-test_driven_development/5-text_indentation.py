#!/usr/bin/python3
"""
This is the TetxIndentation module.

The TextIndentation module provides a simple function text_indentation()
that prints a text with 2 new lines after each characters: ., ? and :.
For example,
>>> text_indentation("Hello.Holbertob?I mean: Holberton")
Hello.$
$
Holbertob?$
$
I mean:$
$
Holberton
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in line:
        if not (i == '.' or i == '?' or i == ':'):
            print("{:s}".format(i), end="")
        else:
            print("{:s}\n".format(i))

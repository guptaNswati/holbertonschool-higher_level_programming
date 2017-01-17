#!/usr/bin/python3
"""
This is the Print#Square module.

The Print#Square module provides a simple function print_square()
that prints a square with the character #
For example,
>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """Print square with #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

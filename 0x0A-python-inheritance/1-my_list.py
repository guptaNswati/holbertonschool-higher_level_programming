#!/usr/bin/python3
"""
This is the subclass MyList. MyList inherits from list.
"""


class MyList(list):
    """
    Print the list in sorted order
    """
    def print_sorted(self):
        print(sorted(self))

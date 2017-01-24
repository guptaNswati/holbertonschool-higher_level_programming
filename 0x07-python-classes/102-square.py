#!/usr/bin/python3
"""
This is a Square class.

The Square class creates a square and calculates its area.
"""


class Square:
    """
    Initialize Square object
    """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not (isinstance(value, int) or isinstance(value, float)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """
    Return area of Square object
    """
    def area(self):
        return (self.size * self.size)

    """
    Compare Square objects
    """
    def __lt__(self, other):
        return (self.size < other.size)

    def __le__(self, other):
        return (self.size <= other.size)

    def __eq__(self, other):
        return (self.size == other.size)

    def __ne__(self, other):
        return (self.size != other.size)

    def __gt__(self, other):
        return (self.size > other.size)

    def __ge__(self, other):
        return (self.size >= other.size)

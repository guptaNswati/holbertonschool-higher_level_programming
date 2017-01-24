#!/usr/bin/python3
"""
This is a Square class.

The Square class creates a square, calculates its area and prints it with #.
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
        if type(value) is not int:
            raise TypeError("size must be an integer")
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
    Print the square with #
    """
    def my_print(self):
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            print()

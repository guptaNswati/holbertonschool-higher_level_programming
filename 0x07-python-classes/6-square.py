#!/usr/bin/python3
"""
This is a Square class.

The Square class creates a square, calculates its area and prints it with #.
"""


class Square:
    """
    Initialize Square object
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise ValueError("size must be an integer")
        if value < 0:
                raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        errMes = "position must be a tuple of 2 positive integers"
        if type(value) is not tuple:
            raise TypeError(errMes)
        if len(value) < 2:
            raise TypeError(errMes)
        if not (type(value[0]) is int and type(value[1]) is int):
            raise TypeError(errMes)
        if (value[0] < 0 or value[1] < 0):
            raise TypeError(errMes)
        self.__position = value

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
        for l in range(self.position[1]):
            print()
        for i in range(self.size):
            for k in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()

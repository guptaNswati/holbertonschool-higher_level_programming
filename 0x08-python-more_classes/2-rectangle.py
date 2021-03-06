#!/usr/bin/python3
"""
This is a Rectangle class.
The Rectangle class creates a Rectangle object which has height and width
and calculates its area and perimeter.
"""


class Rectangle:
    """
    Initialize Rectangle object with height and width.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value

    """
    Calculate area of Rectangle object.
    """
    def area(self):
        return (self.width * self.height)

    """
    Calculate perimeter of Rectangle object.
    """
    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)

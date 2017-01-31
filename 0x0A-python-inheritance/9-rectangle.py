#!/usr/bin/python3
"""
This is the Rectangle class. This class inherits from BaseGeometry class.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Initiate the object with attributes width and height
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    """
    Calculate area of the Rectangle object
    """
    def area(self):
        return self.__width * self.__height

    """
    Return string representation of the Rectangle object
    """
    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

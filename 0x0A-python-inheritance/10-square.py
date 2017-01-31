#!/usr/bin/python3
"""
This is the Square class. The Ssquare class inherits from the Rectangle class.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Initialize Square object
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    """
    Return area of Square object
    """
    def area(self):
        return self.__size * self.__size

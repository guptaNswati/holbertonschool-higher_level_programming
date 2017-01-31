#!/usr/bin/python3
"""
This is the BaseGeometry class.
"""


class BaseGeometry:
    """
    Raise an Exception with a message
    """
    def area(self):
        raise Exception("area() is not implemented")

    """
    Validate value
    """
    def integer_validator(self, name, value):
        if type(name) is not str:
            return
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

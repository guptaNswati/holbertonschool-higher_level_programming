#!/usr/bin/python3
"""
This is a Rectangle class.
The Rectangle class creates a Rectangle object which has height and width
and calculates its area, perimeter and prints it with #.
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    """
    Initialize Rectangle object with height and width.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    """
    Print a Rectangle with #.
    """
    def print(self):
        if (self.width == 0 or self.height == 0):
            print()
            return
        for i in range(self.height):
            for j in range(self.width):
                print("#")
            if i < self.height - 1:
                print()

    """
    Return string representation of Rectangle object.
    """
    def __str__(self):
        out = ""
        if (self.width == 0 or self.height == 0):
            out += "\n"
            return out
        for i in range(self.height):
            for j in range(self.width):
                out += str(Rectangle.print_symbol)
            if i < self.height - 1:
                out += "\n"
        return out

    """
    Return string representation of Rectangle object.
    """
    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")\n"

    """
    Print the message "Bye rectangle..." when a Rectangle object is deleted.
    """
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

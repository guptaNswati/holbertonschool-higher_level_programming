#!/usr/bin/python3
import dis


class MagicClass:
    def __init__(self, radius):
        if not (type(radius) is int or type(radius) is float):
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)

    dis.dis(MagicClass)

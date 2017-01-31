#!/usr/bin/python3
def add_attribute(obj, name, value):
    __slots__ = "{}".format(name)
    setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

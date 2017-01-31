#!/usr/bin/python3
def add_attribute(obj, name, value):
    obj.__dict__[name] = value

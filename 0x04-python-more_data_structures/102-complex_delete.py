#!/usr/bin/python3
def complex_delete(my_dict, value):
    v = list(my_dict.values())
    key = list(my_dict.keys())
    my_dict.pop(key[v.index(value)], None)
    return my_dict

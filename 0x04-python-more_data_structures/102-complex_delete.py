#!/usr/bin/python3
def complex_delete(my_dict, value):
    for k in list(my_dict.keys()):
        if my_dict[k] == value:
            my_dict.pop(k, None)
    return my_dict

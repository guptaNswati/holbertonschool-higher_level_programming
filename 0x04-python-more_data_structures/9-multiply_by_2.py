#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {}
    for k in my_dict:
        new_dict[k] = 2 * my_dict[k]
    return new_dict

#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if not (idx > len(my_list) - 1 or idx < 0):
        my_list[idx] = element
    return my_list

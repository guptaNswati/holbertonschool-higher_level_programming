#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if not idx > len(new_list) or idx < (-1 * len(new_list)):
        new_list[idx] = element
    return new_list

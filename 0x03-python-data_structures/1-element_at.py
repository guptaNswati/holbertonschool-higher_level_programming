#!/usr/bin/python3

def element_at(my_list, idx):
    if idx > len(my_list) or idx < (-1 * len(my_list)):
        return
    return my_list[idx]

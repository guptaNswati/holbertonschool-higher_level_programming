#!/usr/bin/python3
def no_c(str):
    new_str = ""
    for i in str:
        if not (i == 'c' or i == 'C'):
            new_str += i
    return new_str

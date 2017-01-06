#!/usr/bin/python3
def print_alp(i):
    if i < 65 or i > 90:
        return
    repr(chr(i))
    print_alp(i+1)

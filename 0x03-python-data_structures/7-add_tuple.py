#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = 0, 0
    if len(tuple_b) == 0:
        tuple_b = 0, 0
    if len(tuple_a) == 1:
        tuple_a = tuple_a[0], 0
    if len(tuple_b) == 1:
        tuple_b = tuple_b[0], 0
    new_list = []
    i = 0
    while i < 2:
        if tuple_a[i] == "None":
            first = 0
        else:
            first = tuple_a[i]
        if tuple_b[i] == "None":
            second = 0
        else:
            second = tuple_b[i]
        new_list.append(first + second)
        i += 1
    return (new_list[0], new_list[1])

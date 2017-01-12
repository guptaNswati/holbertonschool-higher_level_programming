#!/usr/bin/python3
uniq_add = __import__('2-uniq_add').uniq_add

my_list = [1, 1, 1, 2, 0, 3, 3, 4, 5, 1, 4, 2, 5, 4, 5, 4, 4, 4, 4]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

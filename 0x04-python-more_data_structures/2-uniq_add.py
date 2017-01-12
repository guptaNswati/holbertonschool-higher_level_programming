#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if my_list:
        # a = set(my_list)
        my_list.sort()
        sum += my_list[0]
        for i in range(1, len(my_list)):
            visitd = False
            if my_list[i - 1] == my_list[i]:
                visitd = True
            if not visitd:
                sum += my_list[i]
    return sum

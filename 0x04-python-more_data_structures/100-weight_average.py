#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    if my_list:
        for i in my_list:
            sum += (i[0] + i[1] * 0.1)
        sum = sum / len(my_list)
    return sum

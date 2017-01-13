#!/usr/bin/python3
def weight_average(my_list=[]):
    sum_x = 0
    sum_w = 0
    if my_list:
        for i in my_list:
            sum_x += i[0] * i[1]
            sum_w += i[1]
        sum_x = sum_x / sum_w
    return sum_x

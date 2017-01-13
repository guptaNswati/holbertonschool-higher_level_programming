#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    if my_list:
        for i in my_list:
            sum += float("{}.{}".format(i[0], ''
                                        .join(str(n) for n in str(i[1]))))
        sum = sum / len(my_list)
    return sum

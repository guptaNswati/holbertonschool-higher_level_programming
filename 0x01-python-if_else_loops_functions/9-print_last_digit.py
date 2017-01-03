#!/usr/bin/python3
def print_last_digit(number):
    neg = 0
    if number < 0:
        number *= -1
        neg = 1
    last = number % 10
    if neg == 1:
        number *= -1
    print("{:d}".format(last), end="")
    return last

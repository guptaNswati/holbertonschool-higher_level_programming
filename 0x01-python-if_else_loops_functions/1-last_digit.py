#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg = 0
if number < 0:
    number *= -1
    neg = 1
last = number % 10
if neg == 1:
    number *= -1
    last *= -1
print("Last digit of {:d} is ".format(number), end="")
if last > 5:
    print("{:d} and is greater than 5".format(last))
elif last == 0:
    print("{:d} and is 0".format(last))
else:
    print("{:d} and is less than 6 and not 0".format(last))

#!/usr/bin/python3
i = 122
while i >= 97:
    if i % 2 != 0:
        print(chr(i - 32), end="")
    else:
        print(chr(i), end="")
    i = i - 1

#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ""
    if not str:
        return newStr
    count = 0
    for i in str:
        if n != count:
            newStr += i
        count = count + 1
    return newStr

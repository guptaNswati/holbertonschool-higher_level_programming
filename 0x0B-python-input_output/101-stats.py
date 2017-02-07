#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics.
"""

import sys

def sort_dict(dic):
    for k in sorted(dic.keys()):
        print("{}: {:d}".format(k, dic[k]))
try:
    size = 0
    count = 0
    code = {}
    for line in sys.stdin:
        size += int(line.split()[-1])
        code[line.split()[-2]] = code.get(line.split()[-2], 0) + 1
        count += 1
        if count % 10 == 0:
            print("File size: {:d}".format(size))
            sort_dict(code)
except KeyboardInterrupt as e:
        print("File size: {:d}".format(size))
        sort_dict(code)
        print(e)

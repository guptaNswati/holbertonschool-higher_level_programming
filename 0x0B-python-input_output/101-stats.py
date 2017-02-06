#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics.
"""

import sys
from collections import OrderedDict
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
            print(OrderedDict(sorted(code.items())))
except KeyboardInterrupt as e:
        print("File size: {:d}".format(size))
        print(OrderedDict(sorted(code.items())))
        print(e)

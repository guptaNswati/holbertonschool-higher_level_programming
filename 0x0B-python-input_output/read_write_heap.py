#!/usr/bin/python3
"""
Write a script that finds a string in the heap of a running process, and
replaces it.
"""


import sys
import os

if len(sys.argv) is not 4:
    print("Usage: pid search_string replace_string")
    exit(1)
try:
    os.stat("/proc/" + sys.argv[1])
    with open("/proc/" + sys.argv[1] + "/status", 'r') as f:
        for line in f:
            if line == sys.argv[2]:
                print(sys.argv[3])
except FileNotFoundError:
    print("PID does not exists")
    exit(1)

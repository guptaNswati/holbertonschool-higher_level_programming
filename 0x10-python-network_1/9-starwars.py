#!/usr/bin/python3
"""
This module takes in a string and sends a search request to the Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    count = 0
    names = []
    req = requests.get('http://swapi.co/api/people/?search={:s}'.format(
        sys.argv[1]))
    # check response
    found = req.json()["results"]
    if found:
        for each in found:
            count += 1
            names.append(each['name'])
    print("Number of result: {:d}".format(count))
    for name in names:
        print(name)

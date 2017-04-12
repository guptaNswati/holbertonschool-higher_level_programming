#!/usr/bin/python3
"""
This module takes in a string and sends a search request to the Star Wars API
"""
import requests
import sys


if __name__ == "__main__":
    count = 0
    names = []
    url = 'http://swapi.co/api/people/'
    query = {'search': sys.argv[1]}
    while True:
    # check response
        found = requests.get(url, params=query).json()
        for each in found.get('results'):
            count += 1
            names.append(each.get('name'))
        if found.get('next') is not None:
            url = found.get('next')
        else:
            break
    print("Number of result: {:d}".format(count))
    for name in names:
        print(name)

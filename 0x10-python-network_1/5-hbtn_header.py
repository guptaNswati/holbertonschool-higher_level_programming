#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the value
of the variable X-Request-Id in the response header, using requests package.
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])

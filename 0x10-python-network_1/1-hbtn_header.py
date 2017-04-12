#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the
value of the X-Request-Id variable found in the header of the response.
"""
import urllib.request
import sys


if __name__ == "__main__":
    page, header = urllib.request.urlretrieve(sys.argv[1])
    print(header['X-Request-Id'])

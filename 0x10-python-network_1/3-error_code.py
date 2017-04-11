#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL and displays the body of
the response (decoded in utf-8), handling http error exceptions
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf8"))
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code())

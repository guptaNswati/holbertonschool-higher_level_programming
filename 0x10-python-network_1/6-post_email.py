#!/usr/bin/python3
"""
This module takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and finally displays the body of the
response, using requests package.
"""
import requests
import sys


if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data=payload)
    print(req.text)

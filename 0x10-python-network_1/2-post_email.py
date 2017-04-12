#!/usr/bin/python3
"""
This module takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    to_send = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(to_send)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print(page.decode("utf8"))

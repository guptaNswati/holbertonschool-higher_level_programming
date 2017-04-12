#!/usr/bin/python3
"""
This module contains a script that fetches https://intranet.hbtn.io/status
using urllib package
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
    print("Body response:")
    print("\t- type:", type(page))
    print("\t- content:", page)
    print("\t- utf8 content:", page.decode("utf8"))

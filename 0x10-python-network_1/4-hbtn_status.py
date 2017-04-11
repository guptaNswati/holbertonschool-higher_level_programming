#!/usr/bin/python3
"""
This module fetches https://intranet.hbtn.io/status using request
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("    - type:", type(req.text))
    print("    - content:", req.text)

#!/usr/bin/python3
"""
takes Github credentials (username and password) and uses the Github API to
display the id.
"""
import requests
import sys


if __name__ == "__main__":
    try:
        req = requests.get('https://api.github.com/user',
                           auth=(sys.argv[1], sys.argv[2]))
        print(req.json()["id"])
    except:
        print("None")

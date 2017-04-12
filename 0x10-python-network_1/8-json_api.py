#!/usr/bin/python3
"""
This module that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    payload = {'q': letter}
    req = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        content = req.json()
    except ValueError:
        print("Not a valid JSON")
        sys.exit()
    if content:
        print("[{}] {}".format(content.get('id'), content.get('name')))
    else:
        print("No result")

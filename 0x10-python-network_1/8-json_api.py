#!/usr/bin/python3
"""
This module that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    arg_len = len(sys.argv)
    if arg_len > 2:
        print("No result")
        sys.exit()
    if arg_len == 2:
        if len(sys.argv[1]) > 1:
            print("No result")
            sys.exit()
        try:
            letter = int(sys.argv[1])
            print("No result")
            sys.exit()
        except (TypeError, ValueError):
            letter = sys.argv[1]
    elif arg_len == 1:
        letter = ""
    payload = {'q': letter}
    req = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    content_type = req.headers['Content-Type']
    content_type = content_type[len(content_type)-4:]
    if content_type == 'json' and req.text is not None:
        print("[{:d}] {:s}".format(req.text['id'], req.text['name']))
    else:
        print("Not a valid JSON")

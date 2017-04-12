#!/usr/bin/python3
"""
This module lists 10 commits of given repositories given users commits,
a holberton backend interview question
"""
import requests
import sys


if __name__ == "__main__":
    req = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])).json()
    if req:
        for i, commit in enumerate(req):
            if i < 10:
                if isinstance(commit, dict):
                    print("{}: {}".format(
                        commit.get('sha'),
                        commit.get('commit').get('author').get('name')))
            else:
                break

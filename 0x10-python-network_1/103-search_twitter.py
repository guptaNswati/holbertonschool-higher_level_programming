#!/usr/bin/python3
"""
This module takes in 3 strings and sends a search request to the Twitter API
"""
import requests
import sys
import base64


if __name__ == "__main__":
    bearer_token = "%s:%s" % (sys.argv[1], sys.argv[2])
    token_64 = "Basic %s" % base64.b64encode(bearer_token.encode())
    header = {"Content-Type":
              "application/x-www-form-urlencoded;charset=UTF-8",
              "Authorization": token_64}
    data = {"grant_type": "client_credentials"}
    req = requests.post('https://api.twitter.com/oauth2/token', headers=header,
                        data=data)
    access = req.json().get("access_token")
    url = "https://api.twitter.com/1.1/search/tweets.json"
    headers = {"Authorization": "Bearer %s" % access}
    query = {'q': sys.argv[3], 'count': 5}
    search_req = requests.get(url, params=query, headers=headers)
    search_req = search_req.json().get('statuses')
    for each in search_req:
        print("[{}] {} by {}".format(
            each['id'], each['text'], each['user']['name']))

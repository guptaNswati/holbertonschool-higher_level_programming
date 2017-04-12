#!/usr/bin/python3
"""
This module takes in a string and sends a search request to the Star Wars API.
For each character (people), display a list of movie (film) names
"""
import requests
import sys


if __name__ == "__main__":
    count = 0
    names = {}
    req = requests.get('http://swapi.co/api/people/?search={:s}'.format(
        sys.argv[1]))
    # check response
    found = req.json()["results"]
    if found:
        for each in found:
            movies = each['films']
            if movies:
                films = []
                for movie in movies:
                    films.append(requests.get(movie).json()['title'])
            count += 1
            names[each['name']] = films
    print("Number of result: {:d}".format(count))
    for name in names:
        print(name)
        movies = names[name]
        for movie in movies:
            print("    ", movie)

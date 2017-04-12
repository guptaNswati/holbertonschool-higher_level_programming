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
    url = 'http://swapi.co/api/people/'
    query = {'search': sys.argv[1]}
    while True:
        req = requests.get(url, params=query).json()
        for each in req.get('results'):
            films = []
            for movie in each.get('films'):
                films.append(requests.get(movie).json().get('title'))
            count += 1
            names[each.get('name')] = films
        if req.get('next') is not None:
            url = req.get('next')
        else:
            break
    print("Number of result: {:d}".format(count))
    for name in names:
        print(name)
        movies = names[name]
        for movie in movies:
            print("\t", movie)

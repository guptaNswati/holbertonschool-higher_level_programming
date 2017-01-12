#!/usr/bin/python3
def best_score(my_dict):
    if my_dict:
        v = list(my_dict.values())
        key = list(my_dict.keys())
        return key[v.index(max(v))]

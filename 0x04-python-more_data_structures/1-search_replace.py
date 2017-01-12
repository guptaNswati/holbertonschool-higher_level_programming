#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_lst = []
    if my_list:
        for i in my_list:
            if not i == search:
                new_lst.append(i)
            else:
                new_lst.append(replace)
    return new_lst

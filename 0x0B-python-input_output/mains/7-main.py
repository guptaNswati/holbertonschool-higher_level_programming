#!/usr/bin/python3
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

filemame = "my_list.json"
my_list = [1, 2, 3]
save_to_json_file(my_list, filemame)

filemame = "my_dict.json"
my_dict = { 
    'id': 12,
    'name': "John",
    'places': [ "San Francisco", "Tokyo" ],
    'is_active': True,
    'info': {
        'age': 36,
        'average': 3.14
    }
}
save_to_json_file(my_dict, filemame)

try:
    filemame = "my_set.json"
    my_set = { 132, 3 }
    save_to_json_file(my_set, filemame)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

#!/usr/bin/python3
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filemame = "my_list.json"
my_list = load_from_json_file(filemame)
print(my_list)
print(type(my_list))

filemame = "my_dict.json"
my_dict = load_from_json_file(filemame)
print(my_dict)
print(type(my_dict))

try:
    filemame = "my_set_doesnt_exist.json"
    my_set = load_from_json_file(filemame)
    print(my_set)
    print(type(my_set))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

try:
    filemame = "my_fake.json"
    my_fake = load_from_json_file(filemame)
    print(my_fake)
    print(type(my_fake))
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

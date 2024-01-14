#!/usr/bin/python3
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    list_ = list(load_from_json_file(filename))

except FileNotFoundError:

    save_to_json_file([], filename)
    pass

list_ = list(load_from_json_file(filename))

for i in range(1, len(argv)):

    list_.append(argv[i])

save_to_json_file(list_, filename)

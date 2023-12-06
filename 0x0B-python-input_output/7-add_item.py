#!/usr/bin/python3


"""module to save list in file"""


import json
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == __main__:
    args = sys.argv[1:]

    try:
        existing_data = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_data = []

    existing_data.extend(args)

    save_to_json_file('add_item.json', existing_data)

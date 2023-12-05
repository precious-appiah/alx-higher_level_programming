#!/usr/bin/python3


"""module to write json obj to file"""


import json


def save_to_json_file(my_obj, filename):

    """function to save"""

    with open(filename, 'w', encoding='utf-8') as f:

        return json.dump(my_obj, f)

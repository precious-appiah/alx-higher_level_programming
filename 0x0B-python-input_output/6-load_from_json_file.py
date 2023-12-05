#!/usr/bin/python3


"""module  to convert to json content read from a file"""


import json


def load_from_json_file(filename):

    """function to do that"""

    with open(filename, 'r', encoding='utf-8') as f:

        return json.loads(f.read())

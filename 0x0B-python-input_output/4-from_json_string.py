#!/usr/bin/python3


"""module to deserialize string"""


import json


def from_json_string(my_str):

    """function to deserialise string"""

    return json.loads(my_str)

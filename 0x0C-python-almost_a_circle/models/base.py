#!/usr/bin/python3
"""
module to contain all that we've learnt
"""

import json


class Base:
    """base class for the project"""
    __nb_objects = 0

    def __init__(self, id=None):

        """ constructor """

        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):

        """function to convert list of dicts to json"""

        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        data = json.dumps(list_dictionaries)
        return data

    @classmethod
    def save_to_file(cls, list_objs):

        """class method that saves json rep of pthon obj to file"""

        data = cls.to_json_string(list_objs) if list_objs is not None else []

        filename = f"{cls.__name__}.json"

        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)

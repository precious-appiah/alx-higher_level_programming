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

        if list_objs is None:
            data = '[]'
        else:
            data = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])

        filename = f"{cls.__name__}.json"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(data)

    @staticmethod
    def from_json_string(json_string):

        """function to parse json data"""

        if json_string is not None:
            return json.loads(json_string)
        else:
            return []

    @staticmethod
    def create(cls, **dictionary):

        """function to returns an instance with all
        attributes set using **dictionary"""

        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            raise NotImplementedError("create method not implemented \
                    for class {}".format(cls.__name__))

        dummy_instance.update(**dictionary)
        return dummy_instance

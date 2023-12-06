#!/usr/bin/python3


"""module to define a class"""


class Student:

    """class definition for a student"""

    def __init__(self, first_name, last_name, age):

        """initialization of an instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        """function to retrieve dict in list"""

        json_str = self.__dict__

        if attrs is not None and isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return  {attr: obj.__dict__.get(attr) for attr in attrs if attr in obj.__dict__}
        else:
            return json_str

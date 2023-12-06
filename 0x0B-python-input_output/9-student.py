#!/usr/bin/python3


"""module to define a class"""


class Student:

    """class definition for a student"""

    def __init__(self, first_name, last_name, age):

        """initialization of an instance"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):

            """function"""

            return self.__dict__

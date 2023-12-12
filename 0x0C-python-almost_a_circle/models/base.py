#!/usr/bin/python3


"""
module to contain all that we've learnt
"""


class Base:

    """ base class for the project"""

    __nb_objects = 0

    def __init__(self, id=None):

        """ constructor """

        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        else:
            self.id = id

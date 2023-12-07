#!/usr/bin/python3


"""funct to add attr to an obj"""


def add_attribute(obj, attribute, value):

    """adds new attribute to an object"""

    if '__dict__' in dir(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

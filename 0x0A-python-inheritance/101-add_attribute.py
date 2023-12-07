#!/usr/bin/python3


"""funct to add attr to an obj"""


def add_attr(obj, attr, val):
    """adds new attribute to an object"""
    if '__dict__' in dir(obj):
        setattr(obj, attr, val)
    else:
        raise TypeError("can't add new attribute")

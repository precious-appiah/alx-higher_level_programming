#!/usr/bin/python3


"""funct to add attr to an obj"""

def add_attr(obj, attr, val):

    """adds new attribute"""

    if '__dict__' in dir(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")

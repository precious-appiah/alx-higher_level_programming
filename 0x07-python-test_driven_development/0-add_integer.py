"""module that has functions"""


def add_integer(a, b=98):

    """ this is a function to add integers or float"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

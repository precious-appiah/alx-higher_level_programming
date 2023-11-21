#!/usr/bin/python3
"""Module to define a square class
    Private instance variable size
    instantiation with size
    """


class Square:

    """This is a class doc describong what a square is"""

    def __init__(self, size = 0):

        """this is an init
            size is the private variable
            checks if size is an integer
            check if size is >=0
            """
        self.__size = size
        try:
            if not isinstance (self.__size, int):
                raise TypeError("size must be an integer")
            if size < 0:
                raise ValueError("size must be >= 0")
        except TypeError as err:
            print("{}".format(err))
        except ValueError as err:
            print("{}".format(err))


#!/usr/bin/python3
"""Module to define a square class
    Private instance variable size
    instantiation with size
    """


class Square:

    """This is a class doc describong what a square is"""

    def __init__(self, size=0):

        """this is an init
            size is the private variable
            checks if size is an integer
            check if size is >=0
            """
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, it):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print size passed
        is size is zero print am empty line
        """
        if self.__size == 0:
            print("\n")
        else:
            return '\n'.join('#' * self.__size ** 2 for _in range(self.__size))

    def area(self):
        """public instance method
        that returns area of a square
        """
        return self.__size ** 2

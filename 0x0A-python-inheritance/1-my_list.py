#!/usr/bin/python3


"""module returns list in ascending order """


class MyList(list):

    """base class should have method that returns list"""

    def __init__(self, val):

        """function called when an obj is itialised """

        self.__val = val

    def print_sorted(self):

        """function to print sorted list """

        print(self.val)

#!/usr/bin/python3

""" module describing a class square"""


class Rectangle:

    """ rectangle class that describes a rectangle"""

    def __init__(self, width=0, height=0):

        """init method called when an obj is created"""

        self.__width = width
        self.__height = height

    @property
    def width(self):

        """getter instance attribute width"""

        return self.__width

    @width.setter
    def width(self, width):
        """setter for instance att width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):

        """getter instance attribute height"""

        return self.__height

    @height.setter
    def height(self, height):
        """setter for instance att height"""
        if not isinstance(width, int):
            raise TypeError("height must be an integer")
        elif width < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

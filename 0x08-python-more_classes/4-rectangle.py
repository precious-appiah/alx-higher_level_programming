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
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        rect = ''
        if self.__width == 0 or self.height == 0:
            return ""
        for i in range(self.__height):
            if (i == self.__height - 1):
                rect += '#' * self.__width
            else:
                rect += '#' * self.__width + '\n'
        return rect

    def __repr__(self):
        if self.__width == 0 or self.height == 0:
            return f"R*ectancgle('')"
        return f"Rectangle({self.__width}, {self.__height})"

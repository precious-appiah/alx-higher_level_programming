#!/usr/bin/python3

""" module describing a class square"""


class Rectangle:

    """ rectangle class that describes a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):

        """init method called when an obj is created"""

        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

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
        if isinstance(self.print_symbol, str):
            symbol = self.print_symbol
        if isinstance(self.print_symbol, list):
            symbol = '[' + ', '.join(map(str, self.print_symbol)) + ']'
        for i in range(self.__height):
            if (i == self.__height - 1):
                rect += symbol * self.__width
            else:
                rect += symbol * self.__width + '\n'
        return rect

    def __repr__(self):
        if self.__width == 0 or self.height == 0:
            return f"Rectancgle('')"
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):

        """function for deleting instance of a class"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        """
        class method to check which instace has the
        biggest area
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_1 if rect_1.area() > rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(width=size, height=size)

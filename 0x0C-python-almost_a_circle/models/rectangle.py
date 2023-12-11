#!/usr/bin/python3


""" module to define a rectangle """


from base import Base


class Rectangle(Base):

    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):

        """constructor to class rectangle"""

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):

        """getter for with attr"""

        return self.__width

    @width.setter
    def width(self, width):

        """setter for width"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):

        """getter for height"""

        return self.__width

    @height.setter
    def height(self, height):

        """setter for height"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):

        """getter for x"""

        return self.__x

    @x.setter
    def x(self, x):

        """setter for x"""

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):

        """getter for y"""

        return y

    @y.setter
    def y(self, y):

        """setter for y"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = y

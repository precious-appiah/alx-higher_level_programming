#!/usr/bin/python3
"""
module to define a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor to class rectangle"""

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):

        """getter for with attr"""

        return self.__width

    @width.setter
    def width(self, width):

        """setter for width"""

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):

        """getter for height"""

        return self.__height

    @height.setter
    def height(self, height):

        """setter for height"""

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
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
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):

        """getter for y"""

        return self.__y

    @y.setter
    def y(self, y):

        """setter for y"""

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):

        """return area """

        return self.__width * self.__height

    def display(self):

        """function to primt # height by width"""

        for _ in range(self.__y):
            print()

        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):

        """function to print string in a certain format"""

        return (
                f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
                )

    def update(self, *args, **kwargs):

        """function to update values"""

        if args is not None and len(args) > 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, arg in enumerate(args):
                if i < len(attributes) and arg is not None:
                    setattr(self, attributes[i], arg)

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):

        """assigning values in a dictionary """

        return {
                'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
                }

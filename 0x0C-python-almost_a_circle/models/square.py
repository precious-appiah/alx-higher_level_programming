#!/usr/bin/python3
"""
this is a module to define a square
class square inherits from a rectactangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """this class contanins attributes and methods of a square"""

    def __init__(self, size, x=0, y=0, id=None):

        """function to initialize an instance of square class"""

        super().__init__(size, size, x, y, id)

    def __str__(self):

        """function to return a str"""

        return f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__width}"

    @property
    def size(self):

        """getter to return size"""

        return self.width

    @size.setter
    def size(self, size):

        """setter for size"""

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):

        """function to update params"""

        attributes = ['id', 'size', 'x', 'y']
        if args is not None and len(args > 0):
            for i, arg in enumerate(args):
                if i < len(attributes) and arg is not None:
                    setattr(self, attributes[i], arg)

        for key, value in kwargs.items():
            setattr(self, key, value)

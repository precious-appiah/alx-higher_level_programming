#!/usr/bin/python3


"""
this is a module to define a square
class square inherits from a rectactangle
"""

from rectangle import Rectangle


class Square(Rectangle):

    """this class contanins attributes and methods of a square"""

    def __init__(self, size, x=0, y=0, id=None):
        
        """function to initialize an instance of square class"""

        super().__init__(size, size, x, y, id)

    pass

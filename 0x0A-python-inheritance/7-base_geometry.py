#!/usr/bin/python3


"""module """


class BaseGeometry:

    """defines an empty class"""

    def area(self):

        """function to raise an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        """function to validate in"""

        if isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

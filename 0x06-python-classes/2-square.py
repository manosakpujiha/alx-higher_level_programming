#!/usr/bin/python3

"""

M0dule square

Define class Square

"""





class Square:

    """ Defines a Class square object.

    Private instance attribute: size.

    """



    def __init__(self, size=0):

        """ initialize the method square object

        """

        if not isinstance(size, int):

            raise TypeError("size must be an integer")

        elif size < 0:

            raise ValueError("size must be >= 0")

        else:

            self.__size = int(size)

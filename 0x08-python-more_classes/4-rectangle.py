#!/usr/bin/python3

""" Defines a Rectangle """


class Rectangle:
    """
        Is a 4 sided 2D shape that opposite sides are equal but
        the adjecent sides are not equal

    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def perimeter(self):

        """ 2(width + height)
        """
        if self.__height == 0 or self.__width == 0:
            return 0

        else:
            return (2 * (self.__height + self.__width))

    def area(self):
        """
        width * length
        """
        return (self.__height * self.__width)

    def __str__(self):

        result = []

        if self.__height == 0 or self.__width == 0:
            return ""

        else:
            for i in range(self.__height):
                for x in range(self.__width):
                    result.append("#")
                result.append("\n")

            result.pop()

        return "".join(result)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

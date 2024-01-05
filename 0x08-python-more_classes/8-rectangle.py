#!/usr/bin/python3

class Rectangle:

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

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
                    result.append(str(self.print_symbol))
                result.append("\n")

            result.pop()

        return "".join(result)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_2.area() == rect_1.area():
            return rect_1

        if rect_2.area() > rect_1.area():
            return rect_2

        else:
            return rect_1

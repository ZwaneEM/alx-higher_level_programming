#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):

        if type(value) is not int:
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        
        if type(value) is not int:
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
       
        """ returns area of rectangle """

        return (self.__width * self.__height)

    def display(self):
        """ prints in the stdout the rectangle """

        str_rec = "\n" * self.__y

        for i in range(self.__height):
            str_rec += " " * self.__x
            str_rec += "#" * self.__width + "\n"

        print(str_rec, end="")

    def __str__(self):

        rectangle_name = "[Rectangle] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.__x, self.__y)
        str_wh = "{}/{}".format(self.__width, self.__height)

        return rectangle_name + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):

        """ assigns an argument to each attribute """

        if args is not None and len(args) > 0:
            list_atr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):

        """ returns the dictionary repre of a Rectangle """

        list_attr = ['id', 'width', 'height', 'x', 'y']
        dict_repr = {}

        for i in list_attr:

            dict_repr[i] = getattr(self, i)

        return dict_repr

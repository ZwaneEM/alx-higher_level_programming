#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        
        super().__init__(size, size, x, y, id)

    def __str__(self):

        square_name = "[square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.width)

        return square_name + str_id + str_xy + str_size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):

        if args is not None and len(args) is not 0:

            list_attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if list_attr[i] == 'size':
                    setattr(self, 'height', args[i])
                    setattr(self, 'width', args[i])
                else:
                    setattr(self, list_attr[i], args[i])

        else:
            for key, value in kwargs.items():
                
                if key == 'size':
                    setattr(self, 'height', value)
                    setattr(self, 'width', value)

                else:
                    setattr(self, key, value)


    def to_dictionary(self):
        """ Returns a dictionary with attributes """
        list_atr = ['id', 'size', 'x', 'y']
        dict_res = {}

        for key in list_atr:
            if key == 'size':
                dict_res[key] = getattr(self, 'width')
            else:
                dict_res[key] = getattr(self, key)

        return dict_res

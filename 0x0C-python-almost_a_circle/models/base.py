#!/usr/bin/python3

"""
    base of all other classes
    manages id attribute in all future classes
"""
import json
import csv

class Base():

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):

        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        filename = "Rectangle.json"
        list_new = []

        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(cls.to_json_string(list_new))

        else:
            for i in range(len(list_objs)):
                filename = list_objs[i].__class__.__name__ + ".json"
                with open(filename, "w", encoding="utf-8") as s:

                    list_new.append(list_objs[i].to_dictionary())
                    s.write(cls.to_json_string(list_new))

    @staticmethod
    def from_json_string(json_string):

        if json_string is None or json_string == "":

            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):

        """ Returns an instance with all attributes already set """

        if cls.__name__ == "Rectangle":

            new = cls(30, 30)
        else:
            new = cls(30)

        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        list_ = []

        try:
            filename = cls.__name__ + ".json"

            with open(filename, "r", encoding="utf-8") as f:

                inst_list = cls.from_json_string(f.read())

            for i in range(len(inst_list)):
                list_.append(cls.create(**inst_list[i]))

            return list_

        except FileNotFoundError:
            return list_

    @classmethod
    def save_to_file_csv(cls, list_objs):
        
        list_var = []
        list_app = []
        filename = "Rectangle.csv"

        if list_objs is not None:
            
            if cls.__name__ == "Rectangle":

                list_var.append(['id', 'width', 'height', 'x', 'y'])

                for obj in list_objs:
                    for key in list_var[0]:
                        list_app.append(getattr(obj, key))

                    list_var.append(list_app)
                    list_app = []

            else:
                filename = cls.__name__ + ".csv"

                list_var.append(['id', 'size', 'x', 'y'])

                for obj in list_objs:
                    for key in list_var[0]:
                        list_app.append(getattr(obj, key))

                    list_var.append(list_app)
                    list_app = []

            with open(filename, "w", encoding="utf-8") as file:
                writer = csv.writer(file)

                writer.writerows(list_var)
                    
        else:
            return list_var
        
    @classmethod
    def load_from_file_csv(cls):

        new_list = []
        ret_list = []
        filename = "Rectangle.csv"
        i = 0

        try:
            if cls.__name__ == "Rectangle":

                with open(filename, "r", encoding="utf-8") as file:
                    reader = csv.reader(file)

                    header = next(reader)
                    for row in reader:
                        new_dict = {}
                        for value in row:
                            new_dict[header[i]] = int(value)
                            i += 1
                        new_list.append(new_dict)
                        i = 0


            else:
                filename = cls.__name__ + ".csv"

                with open(filename, "r", encoding="utf-8") as file:
                    reader = csv.reader(file)

                    header = next(reader)
                    for row in reader:
                        new_dict = {}
                        for value in row:
                            new_dict[header[i]] = int(value)
                            i += 1
                        new_list.append(new_dict)
                        i = 0

            for s in range(len(new_list)):
                ret_list.append(cls.create(**new_list[s]))

            return ret_list

        except FileNotFoundError:
            return []

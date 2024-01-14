#!/usr/bin/python3

class Student():

    def __init__(self, first_name, last_name, age):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if not attrs:
            return self.__dict__

        new_dc = {}

        for i in attrs:
            try:
                new_dc[i] = self.__dict__[i]
            except Exception:
                pass
        return new_dc

    def reload_from_json(self, json):

        self.__dict__.update(json)

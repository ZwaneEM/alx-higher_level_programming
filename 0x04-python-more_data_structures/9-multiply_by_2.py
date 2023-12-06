#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dic = {x: a_dictionary[x] * 2 for x in list(a_dictionary)}
    return new_dic

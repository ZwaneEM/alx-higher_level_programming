#!/usr/bin/python3

""" removes all characters c and C from a string """

def no_c(my_string):
    
    my_new_string = ""

    for i in my_string:

        if i != 'c' and i != 'C':
            my_new_string += i

    return my_new_string

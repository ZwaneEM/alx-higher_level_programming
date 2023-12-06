#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):

    sorted_items = sorted(a_dictionary.items())
    for i, v in sorted_items:
        print("{} : {}".format(i, v))

#!/usr/bin/python3

"""
    Appends a string at the end of a text file
    UTF8
    Returns the number of chars added
"""


def append_write(filename="", text=""):

    with open(filename, "a", encoding="utf-8") as f:

        return (f.write(text))

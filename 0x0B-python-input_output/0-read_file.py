#!/usr/bin/python3

"""
    reads a text file and prints it to stdout
"""


def read_file(filename=""):

    with open(filename, "r", encoding="utf-8") as f:

        print("{}".format(f.read()), end="")

    f.close

#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    val = 0

    for i in range(1, len(argv)):
        val += int(argv[i])

    print("{}".format(val))

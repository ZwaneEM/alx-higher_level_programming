#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    leng = len(argv)

    if (leng == 1):
        print("0 arguments.")
        exit()

    if (leng == 2):
        print("1 argument:")

    else:
        print("{} arguments:".format(leng - 1))

    for i in range(1, leng):

        print("{}: {}".format(i, argv[i]))

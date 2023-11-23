#!/usr/bin/python3
""" open file """


def read_file(filename=""):
    """ read file """
    with open(filename, encoding="utf-8") as f:
        out_data = f.read()
        print("{}".format(out_data), end="")

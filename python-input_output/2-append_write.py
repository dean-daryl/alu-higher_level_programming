#!/usr/bin/python3
""" appending to file """


def append_write(filename="", text=""):
    """ append text to given file """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
    return len(text)

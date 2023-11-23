#!/usr/bin/python3
""" json module to access use """
import json
""" convert json string to object """


def from_json_string(my_str):
    """ convert obj to json """
    return json.loads(my_str)

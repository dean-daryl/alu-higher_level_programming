#!/usr/bin/python3
""" Module that contains class Base,
"""
import json


class Base:
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes instances """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Converting a dict into a json string
        """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
            Returns a dict from a string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

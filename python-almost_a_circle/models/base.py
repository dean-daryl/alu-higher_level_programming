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

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
            loading dict representing the parameters for
            and instance and from that creating instances
        """
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
        except:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return instances

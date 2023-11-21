#!/usr/bin/python3
''' Inherits from '''


def inherits_from(obj, a_class):
    '''check if class inherits from the specified class'''
    return type(obj) != a_class and isinstance(obj, a_class)

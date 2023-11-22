#!/usr/bin/python3
"""
Geometry class
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Implement rectangle class"""
    def __init__(self, width, height):
        """Define rectangle"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """output"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))

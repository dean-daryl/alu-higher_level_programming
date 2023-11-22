#!/usr/bin/python3
"""
Geometry class
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Implement rectangle class"""
    def __init__(self, width, height):
        """Define rectangle"""
        self.integer_validator(self, "width", width)
        self.__width = width
        self.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """output"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))

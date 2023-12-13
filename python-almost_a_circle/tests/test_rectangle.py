#!/usr/bin/python3
""" Module for test Rectangle class """
import unittest
import os
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethods(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method called for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Test all new rectangle """
        new = Rectangle(1, 2)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 2)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

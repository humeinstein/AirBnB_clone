#!/usr/bin/python3
""" Unittesting for BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid
from models.state import State
import pep8

class test_state(unittest.TestCase):
    """ test file """
    def test_pep8(self):
        """ test pep8 """

        pep8check = pep8.StyleGuide(quiet=True)
        check = pep8check.check_files(["models/state.py"])
        self.assertEqual(check.total_errors, 0,
                "Found code errors")
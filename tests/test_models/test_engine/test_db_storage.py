#!/usr/bin/python3
""" . """
from models.engine.db_storage import DBStorage
from models.engine import db_storage
from models.__init__ import storage
from unittest.mock import patch
from io import StringIO
import console
import unittest
import pep8
import sys
from os import getenv
import MySQLdb
import models
import unittest


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'can not run file')
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'models/engine/db_storage.py'
        file2 = 'tests/test_models/test_engine/test_db_storage.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'can not run file')
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(db_storage.__doc__) > 0)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'can not run file')
    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(DBStorage.__doc__) > 0)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'can not run file')
    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(DBStorage):
            self.assertTrue(len(func.__doc__) > 0)


@unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db', 'can not run file')
class TestDBStorage(unittest.TestCase):
    """ Check for functionaly of Console. """
    def setUp(self):
        """Setting Up """
        self.console_o = DBStorage()

    def tearDown(self):
        """Cleaning up after each test. """
        pass

if __name__ == "__main__":
    unittest.main()

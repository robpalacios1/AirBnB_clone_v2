#!/usr/bin/python3
""" . """
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage
from console import HBNBCommand
from unittest.mock import patch
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.state import State
from models.city import City
from models.user import User
from io import StringIO
import MySQLdb
import console
import unittest
import pep8
import sys
import os


class TestPep8B(unittest.TestCase):
    """ Check for pep8 validation. """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ Check for documentation. """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(console.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(HBNBCommand):
            self.assertTrue(len(func.__doc__) > 0)


class TestConsole(unittest.TestCase):
    """ Check for functionaly of Console. """
    def setUp(self):
        """Setting Up """
        self.console_o = HBNBCommand()

    def tearDown(self):
        """Cleaning up after each test. """
        pass

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', 'for databases')
    def test_create(self):
        """ . """
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create User")
            lenn = len(out.getvalue())
            self.assertTrue(lenn > 0)
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create Lauca")
            self.assertEqual("** class doesn't exist **\n", out.getvalue())
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create")
            self.assertEqual("** class name missing **\n", out.getvalue())
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("all State")
            lenn = len(out.getvalue())
            self.assertTrue(lenn > 0)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'for file')
    def test_create(self):
        """ . """
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create User")
            lenn = len(out.getvalue())
            self.assertTrue(lenn > 0)
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create Lauca")
            self.assertEqual("** class doesn't exist **\n", out.getvalue())
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("create")
            self.assertEqual("** class name missing **\n", out.getvalue())
        with patch("sys.stdout", new=StringIO()) as out:
            self.console_o.onecmd("all State")
            lenn = len(out.getvalue())
            self.assertTrue(lenn > 0)


if __name__ == "__main__":
    unittest.main()

# python3 -m unittest discover tests
# python3 -m unittest tests/test_models/test_base_model.py

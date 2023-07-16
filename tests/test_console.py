#!/usr/bin/python3
"""
A test file for the console module
"""
from console import HBNBCommand
from models.engine.file_storage import FileStorage
import unittest
from unittest.mock import patch
import os
import sys
from models import storage
from io import StringIO


class TestHBNBCommand(unittest.TestCase):
    """
    A test class for the console module
    """

    def setUp(self):
        """
        Is executed first before any other tests
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def tearDown(self):
        """
        Is executed last after all tests have been performed
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_prompt(self):
        """
        Checks if the prompt is well displayed
        """
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    def test_empty_line(self):
        """
        Tests an empty command
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

    def test_help(self):
        """
        Tests the help command
        """
        h = ("Documented commands (type help <topic>):\n"
             "========================================\n"
             "EOF  all  count  create  destroy  help  quit  show  update")
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(h, output.getvalue().strip())

    def test_count(self):
        """
        Tests the count Method of  the console module
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(len(output.getvalue()) > 0)

    def test_create(self):
        """
        tests the create method
        """
        # errors are correctly displayed
        error = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(error, output.getvalue().strip())

        error = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create Model"))
            self.assertEqual(error, output.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertLess(0, len(output.getvalue().strip()))
            testKey = "State.{}".format(output.getvalue().strip())
            self.assertIn(testKey, storage.all().keys())

    def test_show(self):
        """
        Tests for the show command
        """
        error = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual(error, output.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             output.getvalue())
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(output.getvalue() == "** instance id missing **\n")

    def test_all(self):
        """
        Tests the all method of the console module
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(output.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('User.all()')
            self.assertTrue(len(output.getvalue()) > 0)

    def test_destroy(self):
        """
        Test method for the destroy method
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(output.getvalue() == "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd('all FakeClass')
            self.assertTrue(output.getvalue() == "** class doesn't exist **\n")

    def test_update(self):
        """
        tests the update method
        """
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("sldkfjsl.update()")
            self.assertEqual("** class doesn't exist **\n", output.getvalue())

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.update(54664565465)")
            self.assertEqual("** no instance found **\n", output.getvalue())

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("create User")

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("all User")
            obj = output.getvalue()
        obj_id = obj[obj.find('(')+1:obj.find(')')]

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.update(" + obj_id + ")")
            self.assertEqual("** attribute name missing **\n",
                             output.getvalue())

        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("User.update(" + obj_id + ", name)")
            self.assertEqual("** value missing **\n",
                             output.getvalue())

    def test_quit(self):
        """
        Tests the quit method
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_exits(self):
        """
        Tests the EOF method
        """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertTrue(HBNBCommand().onecmd("EOF"))

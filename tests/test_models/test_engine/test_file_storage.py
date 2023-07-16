#!/usr/bin/python3
"""
A unit test module for the file storage module
"""
import unittest
from datetime import datetime
from models import storage
import os
import json

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    A Test class for the FileStorage class
    """

    def setUp(self):
        """
        Removes any existing file.json file
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def tearDown(self):
        """
        Removes any file created after execution of the test
        """
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_init(self):
        """
        Tests if  the instantiation method works correctly
        """
        store_test = FileStorage()
        self.assertIsInstance(store_test, FileStorage)

    def test_all(self):
        """
        Tests if it returns all objects created from all classes
        """
        storage.reload()
        inst = BaseModel()
        storage.new(inst)
        inst = User()
        storage.new(inst)
        inst = City()
        storage.new(inst)
        inst = State()
        storage.new(inst)
        inst = Amenity()
        storage.new(inst)
        inst = Place()
        storage.new(inst)
        inst = Review()
        storage.new(inst)
        obj = storage.all()
        self.assertGreaterEqual(len(obj), 7)
        self.assertEqual(type(obj), dict)
        # check if error on arguments provided
        with self.assertRaises(TypeError):
            storage.all(inst)
        with self.assertRaises(TypeError):
            storage.all(None)

    def test_new(self):
        """
        Test the new method of the FileStorage class
        """
        inst = User()
        storage.new(inst)
        self.assertGreaterEqual(len(storage.all()), 8)
        self.assertIn("User." + inst.id, storage.all().keys())
        # more than one argument provided
        with self.assertRaises(TypeError):
            storage.new(inst, inst)

    def test_save(self):
        """
        Tests the save method for the FileStorage class
        """
        inst = User()
        self.assertFalse(os.path.isfile('file.json'))
        storage.save()
        self.assertTrue(os.path.isfile('file.json'))
        # arguments provided
        with self.assertRaises(TypeError):
            storage.save(inst)

    def test_reload(self):
        """
        Tests the reload method of the FileStorage class
        """
        inst = City()
        with open("file.json", "w", encoding="utf-8") as file_open:
            key = "{}.{}".format(type(inst).__name__, inst.id)
            file_open.write(json.dumps({key: inst.to_dict()}))
        storage.reload()
        obj = FileStorage._FileStorage__objects
        self.assertIn("City." + inst.id, obj)

        # check for errors
        with self.assertRaises(TypeError):
            storage.reload(inst)
        with self.assertRaises(TypeError):
            storage.reload(inst, None)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""
A module that serializes instances to JSON file
Also deserializes JSON file to an instance
"""
import json
import os


class FileStorage:
    """
    This instance is responsible for storing and retrieving JSON strings
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        An instance method that returns a dictionary of all objects stored in
        private class attribute '__objects'
        """

        return self.__objects

    def new(self, obj):
        """
        An instance method that sets the '__objects' with the obj argument
        """

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Saves(serializes) the objects to the json file in given path
        """

        temp = {}  # temporary dictionary to hold the values for each item

        for key, value in self.__objects.items():
            temp[key] = value.to_dict()

        # save the dictionary as a json file
        with open(self.__file_path, "w") as file_write:
            file_write.write(json.dumps(temp))

    def reload(self):
        """
        Retrieves(deserializes) the JSON file to '__objects' attribute
        """
        from models.base_model import BaseModel

        if os.path.isfile(self.__file_path):
            # open the file as read only
            with open(self.__file_path, "r") as file_read:
                temp = json.loads(file_read.read())  # load the json string
                self.__objects = {}  # initialize it as empty
                # create objects from the json file extracts
                for key, value in temp.items():
                    self.__objects[key] = BaseModel(**value)
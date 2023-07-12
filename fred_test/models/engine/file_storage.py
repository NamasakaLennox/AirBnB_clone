#!/usr/bin/python3
"""
A module that contains the file storage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """The file storage class"""
    __file_path = "./store.json"
    __objects = {}

    def all(self):
        """Function that returns the dictionary `__objects`"""
        return self.__objects

    def new(self, obj):
        """
        Function that sets in `__objects` the `obj` with key
        `<obj class name>.id`
        Args:
            obj(class) - the instance to be saved
        """
        new_key = obj.to_dict()['__class__'] + '.' + obj.id
        self.__objects[new_key] = obj

    def save(self):
        """
        Function that serializes __objects to JSON in
        the `__file_path`
        """
        with open(self.__file_path, "w") as fstore:
            tmp_dict = {}
            for key, value in self.__objects.items():
                tmp_dict[key] = value.to_dict()

            json.dump(tmp_dict, fstore)

    def reload(self):
        """
        Function that deserializes the JSON file to `__objects`
        (only if the JSON `__file_path` exists)
        """
        try:
            with open(self.__file_path, "r") as fstore:
                st_objs = json.load(fstore)
                for key, value in st_objs.items():
                    self.__objects[key] = BaseModel(**value)
        except Exception:
            pass

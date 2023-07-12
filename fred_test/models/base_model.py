#!/usr/bin/python3
"""
A module that contains the Base class
"""
import datetime
import uuid
from models import storage


class BaseModel:
    """
    A class that defines all common attributes/methods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """Function that initiates the class instance"""

        if len(kwargs.keys()) > 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key in ["created_at", "updated_at"]:
                    value = datetime.datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.my_number = None
            self.name = ""
            self.id ="{}".format(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

    def __str__(self) -> str:
        """Prints the string representation of class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Function that saves the instance of this class"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """
        Function that returns the dictionary representation of the
        class
        """
        attr = ["my_number", "name", "__class__", "updated_at", "id",
                "created_at" ]
        dict_attr = {}

        for key in attr:
            if key == "__class__":
                dict_attr[key] = self.__class__.__name__
                continue
            if key == 'my_number':
                dict_attr[key] = getattr(self, key)
                continue
            dict_attr[key] ="{}".format(getattr(self, key))

        return dict_attr

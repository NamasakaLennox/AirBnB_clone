#!/usr/bin/python3
"""
Defines the common attributes/methods for other classes
It is the base class for all classes that inherit from it
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):
        """
        Constructor that initializes the instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        instance method that defines the string output
        """
        string = "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                       self.__dict__)
        return (string)

    def save(self):
        """
        An instance method that sets the updated time of the class instance
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        output = self.__dict__.copy()
        output['__class__'] = self.__class__.__name__
        output['created_at'] = self.created_at.isoformat()
        output['updated_at'] = self.updated_at.isoformat()
        return (output)

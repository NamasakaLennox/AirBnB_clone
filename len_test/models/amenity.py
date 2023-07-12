#!/usr/bin/python3
"""
Contains a class Amenity that inherits from the BaseModel class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Manages attributes of the Amenities
    Inherits attributes of the BaseModel Class
    """

    name = ""

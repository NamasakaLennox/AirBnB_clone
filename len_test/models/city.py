#!/usr/bin/python3
"""
Contains a class City that inherits from the BaseModel class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class to manage Cities
    Inherits attributes of the BaseModel Class
    """

    state_id = ""
    name = ""

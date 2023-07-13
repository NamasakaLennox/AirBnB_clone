#!/usr/bin/python3
"""
Module that contains the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that is City class
    Inherits:
        BaseModel (Class)
    """
    state_id = ""
    name = ""
    pass

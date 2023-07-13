#!/usr/bin/python3
"""
Module that contains the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that is Review class
    Inherits:
        BaseModel (Class)
    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
    pass

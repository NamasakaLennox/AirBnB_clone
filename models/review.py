#!/usr/bin/python3
"""
Contains a class Review that inherits from the BaseModel class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Manages attributes of the class Review
    Inherits attributes of the BaseModel Class
    """

    place_id = ""
    user_id = ""
    text = ""

#!/usr/bin/python3
"""
Module for the class User that inherits from the BaseModel class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    A User class that inherits from the BaseModel class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

#!/usr/bin/python3
"""Model that contains a class User
"""
from models.base_model import BaseModel 


class User(BaseModel):
    """A user class
    Inherits:
        BaseModel (class) 
    """
    email : str = ""
    password : str = ""
    first_name : str = ""
    last_name : str = ""
    pass
#!/usr/bin/python3
""" Class Review (child class of BaseModel)"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class that inherits BaseMode l """
    place_id = ""
    user_id = ""
    text = ""

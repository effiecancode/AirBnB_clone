#!/usr/bin/python3
""" Class Amenity (child class of BaseModel)"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits BaseMode l"""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

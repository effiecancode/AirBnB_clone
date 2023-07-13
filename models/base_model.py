#! /usr/bin/python3
"""base class"""

import datetime
from uuid import uuid4


class BaseModel:
    """actual base class"""

    def __init__(self):
        """instance of base class"""
        self.id = str(uuid4())
        self.created_at = datetime.datetime.now().isoformat()
        self.updated_at = datetime.datetime.now().isoformat()

    def __str__(self):
        """magic method __str__ to print [<class name>] (<self.id>)
          <self.__dict__>	"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updated the public instance attribute with current time"""
        self.updated_at = datetime.now

    def to_dict(self):
        """function to return a dictionary containign all
        keys/values of __dict__ of the instance"""
        dictf = self.__dict__.copy()
        """identify the class name of the instance"""
        dictf["__class__"] = self.__class__.__name__
        return dictf

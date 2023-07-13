#! /usr/bin/python3
"""base class"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """actual base class"""

    def __init__(self, *ars, **kwargs):
        """instance of base class"""
        if kwargs:
            del kwargs["__class__"]
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    new_val = val.isoformat()
                    setattr(self, key, new_val)
                else:
                    setattr(self, key, val)

        else:
            self.id = str(uuid4())
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

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

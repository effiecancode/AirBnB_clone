#! /usr/bin/python3
"""base class"""
from datetime import datetime
from uuid import uuid4
# import models
import models


class BaseModel:
    """actual base class"""

    # def __init__(self, *args, **kwargs):
    #     """instance of base class"""
    #     if kwargs:
    #         del kwargs["__class__"]
    #         for key, val in kwargs.items():
    #             if key == "created_at" or key == "updated_at":
    #                 new_val = val.isoformat()
    #                 setattr(self, key, new_val)
    #             else:
    #                 setattr(self, key, val)

    #     else:
    #         self.id = str(uuid4())
    #         self.created_at = datetime.now()
    #         self.updated_at = datetime.now()
    #         storage.new(self)

    def __init__(self, *args, **kwargs):
        """ Construct """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """magic method __str__ to print [<class name>] (<self.id>)
          <self.__dict__>	"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updated the public instance attribute with current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """function to return a dictionary containign all
        keys/values of __dict__ of the instance"""
        dictf = self.__dict__.copy()
        """identify the class name of the instance"""
        dictf["__class__"] = self.__class__.__name__
        dictf['created_at'] = self.created_at.isoformat()
        dictf['updated_at'] = self.updated_at.isoformat()
        return dictf

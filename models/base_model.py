#!/usr/bin/python3
"""Base model"""
import uuid
from datetime import datetime as dt


f = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """actual base class"""
    def __init__(self, *args, **kwargs):
        """ Construct anew instance """
        if kwargs:
            if 'created_at' in kwargs:
                kwargs['created_at'] = dt.strptime(kwargs['created_at'], f)
            if 'updated_at' in kwargs:
                kwargs['updated_at'] = dt.strptime(kwargs['updated_at'], f)
            kwargs.pop('__class__', None)
            self.__dict__ = kwargs
        else:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
            storage.new(self)

    def __str__(self):
        """magic method __str__ to print [<class name>] (<self.id>)
          <self.__dict__>	"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updated the public instance attribute with current time"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """function to return a dictionary containign all
        keys/values of __dict__ of the instance"""
        dictf = self.__dict__.copy()
        """identify the class name of the instance"""
        dictf["__class__"] = self.__class__.__name__
        dictf['created_at'] = self.created_at.isoformat()
        dictf['updated_at'] = self.updated_at.isoformat()
        return dictf

#! /usr/bin/python3
""" Contains the FileStorage class to implement the flow:
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
<class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'>
-> <class 'BaseModel'>
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ FileStorage class, serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in dict __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objdict = {}
        for k, v in FileStorage.__objects.items():
            objdict[k] = v.to_dict()

            with open(FileStorage.__file_path, "w", encoding="utf-8") as jfile:
                json.dump(objdict, jfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        dict_mapper = {"MyBase": BaseModel}

        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as jsonf:
                Deserialized = json.load(jsonf)
                for obj_v in Deserialized.values():
                    Cls_name = obj_v["__class__"]
                    Cls_object = dict_mapper[Cls_name]
                    self.new(Cls_object(**obj_v))

        except FileNotFoundError:
            pass

#!/usr/bin/python3
""" Contains the FileStorage Class to implement the flow:
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
<class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'>
-> <class 'BaseModel'>
"""
import json


class FileStorage:
    """ FileStorage class, serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in dict __objects the obj with key <obj class name>.id """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objdict = {}
        for k, v in self.__objects.items():
            objdict[k] = v.to_dict()

            with open(self.__file_path, "w", encoding="utf-8") as jfile:
                json.dump(objdict, jfile)

    def reload(self):
        """handle reload"""
        from base_model import BaseModel

        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    if class_name == 'BaseModel':
                        obj = BaseModel(**value)
                    else:
                        """ Handle other classes"""
                        continue
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

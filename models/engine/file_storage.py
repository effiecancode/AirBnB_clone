#!/usr/bin/python3
""" Contains the FileStorage class to implement the flow:
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> JSON dump ->
<class 'str'> -> FILE -> <class 'str'> -> JSON load -> <class 'dict'>
-> <class 'BaseModel'>
"""
import json
# # from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review


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
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        # try:
        #     with open(self.__file_path, 'r') as file:
        #         obj_dict = json.load(file)
        #         for key, value in obj_dict.items():
        #             class_name = value['__class__']
        #             if class_name == 'BaseModel':
        #                 obj = BaseModel(**value)
        #             else:
        #                 """ Handle other classes"""
        #                 continue
        #             self.__objects[key] = obj
        # except FileNotFoundError:
        #     pass
        classes = {
                    "State": State, "Amenity": Amenity, "Review": Review,
                    "BaseModel": BaseModel, "City": City, "Place": Place, "User": User
                }
        file_name = self.__file_path
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                str_json = f.read()
                dict_obj = json.loads(str_json)

                for k in dict_obj:
                    self.__objects[k] = classes[dict_obj[k]["__class__"]](
                        **dict_obj[k]
                    )

        except FileNotFoundError:
            pass

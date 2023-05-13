#!/usr/bin/python3
"""module with the class FileStorage"""

import json
import os


class FileStorage:
    """serializes instances to a JSON file and\
            deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        cl_name = obj.__class__.__name__
        base_id = obj.id
        dic_key = "{}.{}".format(cl_name, base_id)
        FileStorage.__objects[dic_key] = obj

    def save(self):
        """serializes __objects to the JSON file(path: __file_path)"""
        dic = {}
        for k, v in FileStorage.__objects.items():
            dic[k] = v.to_dict()

        to_json = json.dumps(dic)
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            f.write(to_json)

    def reload(self):
        """deserializes the JSON file to __objects\
                (only if the JSON file(__file_path) exists
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.amenity import Amenity
        from models.review import Review

        cls_dic = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'Amenity': Amenity, 'Review': Review}
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as f:
                from_json = json.load(f)
                for k, v in from_json.items():
                    cls_name = v['__class__']
                    self.new(cls_dic[cls_name](**v))

#!/usr/bin/python3

""" This is the File Storage module."""

import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:

    """The file storage class """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ It returns the dictionary __objects """

        return (self.__objects)

    def new(self, obj):

        """
        sets in __objects the obj with key
        <obj class name>.id

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, "w") as files:
            json.dump(serialized_objects, files)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as files:
                data = json.load(files)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    cls = eval(class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

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
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, 'w') as json_file:
            tmp_dict = {}
            for key, value in self.__objects.items():
                tmp_dict[key] = value.to_dict()
            json.dump(tmp_dict, json_file)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, 'r') as rt_json:
                for obj in json.load(rt_json).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return

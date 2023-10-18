#!/usr/bin/python3

""" This module defines the Basemodel class """

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:

    """ The BaseModel for the AirBnb Project """
    
    def __init__(self, *args, **kwargs):

    """
        This function initializes a new BaseModel
        
        Args:
                *args (any): unused.
                **kwargs (dict): Key/value pairs of attributes
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, t_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)
    def __str__(self):
        
        """ function that return a string version of the class """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    def save(self):
        
        """ Function that update the public instance attribute updated_at to current datetime """
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        
        """
        Return the dictionary of the BaseModel instance.
        Includes the key/value pair __class__ representing
        the class name of the object.

        """
        rt_dict = self.__dict__.copy()
        rt_dict["created_at"] = self.created_at.isoformat()
        rt_dict["updated_at"] = self.updated_at.isoformat()
        rt_dict["__class__"] = self.__class__.__name__
        return (rt_dict)

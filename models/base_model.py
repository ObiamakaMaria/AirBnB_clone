#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new instance. """
        if kwargs:
            for key, value in kwargs.item():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
    def save(self):
        """Update the updated_at attribute with the current date time. """
        self.update_at - datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the instance."""
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        obj_dict["__clas__"] = self.__class__.__name__
        return obj_dict
    
    def __str__(self):
        """Return a string representaiton of the instance."""
         return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

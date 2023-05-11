#!/usr/bin/python3
"""A module with a class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """a class that defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """instantiation of public instance attributes using *args, **kwargs arguments"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key == 'created_at' or key == 'updated_at':
                    self.created_at = datetime.fromisoformat(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """returns a string format for the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns ta dictionary containing all keys/values of __dict__ of the instance"""
        new_dict = {}
        new_dict['__class__'] = self.__class__.__name__

        for key, value in self.__dict__.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value

        return new_dict

#!/usr/bin/python3
"""A module with a class BaseModel"""

import uuid
from datetime import datetime


class BaseModel:
    """a class that defines all common attributes/methods for other classes"""

    def __init__(self):
        """instantiation of public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
        new_dict['updated_at'] = self.updated_at.isoformat()
        new_dict['created_at'] = self.created_at.isoformat()

        for key, value in self.__dict__.items():
            new_dict[key] = value

        return new_dict

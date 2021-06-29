#!/usr/bin/python3
"""Hola"""
import uuid
import models
from datetime import datetime
from models.engine.file_storage import FileStorage

class BaseModel:
    """ Class base model """
    def __init__(self, *args, **kwargs):
        """ constructor for base model """
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            FileStorage.new(self)

    def __str__(self):
        """ return string of the instance """
        str_n = "[BaseModel] ({}) {}"\
            .format(self.id, self.__dict__)
        return str_n

    def save(self):
        """ save """
        self.updated_at = datetime.now()
        FileStorage.save()

    def to_dict(self):
        """ convert to dict """
        new_dict = {}
        for key in self.__dict__:
            new_key = key.replace("_BaseModel__", "")
            new_dict[new_key] = self.__dict__[key]
        new_dict["id"] = self.id
        new_dict["__class__"] = str(self.__class__.__name__)
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict

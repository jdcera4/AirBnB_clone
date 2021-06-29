#!/usr/bin/python3
'''Module for file_storage class'''
from models.amenity import Amenity
from models.base_model import BaseModel
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        obj_key = "{}.{}".format(obj.__class__.name, obj.id)
        self.__objects[obj_key] = obj

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        new_dict = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, f)

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
         no exception should be raised)'''
        pass

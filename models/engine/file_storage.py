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
    __file_path = ""
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <obj class name>.id'''
        pass

    def save(self):
        '''serializes __objects to the JSON file (path: __file_path)'''
        pass

    def reload(self):
        '''deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
         no exception should be raised)'''
        pass

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
    def __init__(self):
        pass

    def all(self):
        pass

    def new(self, obj):
        pass

    def save(self):
        pass

    def reload(self):
        pass

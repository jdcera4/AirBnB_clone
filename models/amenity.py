#!/usr/bin/python3
""" no modeule """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ class """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

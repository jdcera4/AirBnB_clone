#!/usr/bin/python3
""" Module for state class """
from models.base_model import BaseModel


class State(BaseModel):
    """ Class State """
    name = ""

    def __init__(self, *args, **kwargs):
        '''constructor for state'''
        super().__init__(*args, **kwargs)

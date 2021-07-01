#!/usr/bin/python3
""" """
# from models.city import city
from models.user import User
from models.amenity import Amenity
from models.base_model import BaseModel


class Place(BaseModel):
    """ Class for Place """
    name = ""
    user_id = ""
    city_id = ""
    description = ""
    max_guest = 0
    price_by_night = 0
    number_rooms = 0
    number_bathrooms = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

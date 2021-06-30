#!/usr/bin/python3
""" """
# from models.city import city
from models.user import User
from models.amenity import Amenity


class Place:
    """ Class for Place """
    user_id = ""
    city_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

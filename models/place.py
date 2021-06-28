#!/usr/bin/python3
""" """
from models.city import city
from models.users import Users
from models.amenity import Amenity


class Place:
    """ Class for Place """
    user_id = User.id
    city_id = City.id
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = Amenity.id

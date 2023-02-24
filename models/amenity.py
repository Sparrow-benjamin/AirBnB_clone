#!/usr/bin/python3
""" Class Amenity that inherits from base model"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class Amenity that inherits from base model """
    name = ""

    def _init_(self, *args, **kwargs):
        """ Constructor """
        super()._init_(self, *args, **kwargs)


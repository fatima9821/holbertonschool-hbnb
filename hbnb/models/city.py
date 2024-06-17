#!/usr/bin/python3
""" create city """
from datetime import datetime
from models.base_models import BaseModel
import uuid


class City(BaseModel):
    def __init__(self, city_id, name, country_id):
        super().__init__()
        if not id or not name:
            raise TypeError("id, name and country are required")
        self.city_id = ()
        self.name = ()
        self.country_id = ()
        self.created_at = datetime.now()
        self.created_at = datetime.now()
        self.places = []

    def add_place(self, place):
        self.places.append(place)

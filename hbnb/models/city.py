#!/usr/bin/python3
""" create city """
from datetime import datetime
import uuid


class City:
    def __init__(self, id, name, country):
        if not id or not name:
            raise TypeError("id, name and country are required")
        self.id = ()
        self.name = ()
        self.country = ()
        self.created_at = datetime.now()
        self.created_at = datetime.now()
        self.places = []

    def add_place(self, place):
        self.places.append(place)

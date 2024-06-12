#!/usr/bin/python3
""" create city """
from datetime import datetime
import uuid


class City:
    def __init__(self, id, name, country):
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.country = country
        self.created_at = datetime.now()
        self.created_at = datetime.now()
        self.places = []

    def add_place(self, place):
        self.places.append(place)

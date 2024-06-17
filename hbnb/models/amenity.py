#!/usr/bin/python3
""" create amenity """
from datetime import datetime
import uuid


class Amenity:
    def __init__(self, name):
        super().__init__()
        if not name:
            raise TypeError("id  and name are required")
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

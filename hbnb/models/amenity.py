#!/usr/bin/python3
""" create amenity """
from datetime import datetime
import uuid


class Amenity:
    def __init__(self, id, name):
        if not id or not name:
            raise TypeError("id  and name are required")
        self.id = id or str(uuid.uuid4())
        self.name = name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

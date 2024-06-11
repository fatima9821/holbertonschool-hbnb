#!/usr/bin/python3
""" creation de la place """
from datetime import datetime
import uuid


class Place:
    def __init__(self, id, name, description, address, city, latitude,
                 longitude, host, number_of_rooms, bathrooms,
                 price_per_night, max_guests):
        self.id = id or str(uuid.uuid4())
        self.name = str
        self.description = str
        self.address = str
        self.city = city
        self.latitude = float
        self.longitude = float
        self.host = str
        self.number_of_rooms = int
        self.bathrooms = int
        self.price_per_night = int
        self.max_guests = int
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

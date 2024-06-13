#!/usr/bin/python3
""" creation de la place """
from datetime import datetime
import uuid


class Place:
    def __init__(self, id, name, description, address, city, latitude,
                 longitude, host, number_of_rooms, bathrooms,
                 price_per_night, max_guests):
        self.id = ()
        self.name = ()
        self.description = ()
        self.address = ()
        self.city = ()
        self.latitude = ()
        self.longitude = ()
        self.host = ()
        self.number_of_rooms = ()
        self.bathrooms = ()
        self.price_per_night = ()
        self.max_guests = ()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

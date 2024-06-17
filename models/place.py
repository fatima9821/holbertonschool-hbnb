#!/usr/bin/python3
""" creation de la place """
from models.base_models import BaseModel
from datetime import datetime
from uuid import uuid4

class Place(BaseModel):
    def __init__(self,place_id, name, description, address, city_id, latitude,
                 longitude, host_id, number_of_rooms, bathrooms,
                 price_per_night, max_guests):
        super().__init__()
        self.place_id = uuid4
        self.name = name
        self.description = description
        self.address = address
        self.city_id = uuid4
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = uuid4
        self.number_of_rooms = number_of_rooms
        self.bathrooms = bathrooms
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.reviews = []
        self.amenities = []

    def add_review(self, review_id):
        if review_id not in self.reviews:
            self.reviews.append(review_id)

    def add_amenity(self, amenity):
        if amenity_id not in self.amenities:
            self.amenities.append(amenity_id)

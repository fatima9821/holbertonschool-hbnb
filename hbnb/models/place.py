#!/usr/bin/python3
""" creation de la place """
from .base_models import BaseModel


class Place(BaseModel):
    def __init__(self, id, name, description, address, city, latitude,
                 longitude, host, number_of_rooms, bathrooms,
                 price_per_night, max_guests):
        super().__init__()
        self.id = ()
        self.name = ()
        self.description = ()
        self.address = ()
        self.city_id = ()
        self.latitude = ()
        self.longitude = ()
        self.host_id = ()
        self.number_of_rooms = ()
        self.bathrooms = ()
        self.price_per_night = ()
        self.max_guests = ()
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

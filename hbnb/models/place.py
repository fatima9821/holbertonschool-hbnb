#!/usr/bin/python3
""" creation de la place """


class Place:
    def __init__(self, id, name, description, price, owner):        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)

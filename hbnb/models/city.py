#!/usr/bin/python3
""" create city """


class City:
    def __init__(self, id, name, country):
        self.id = id
        self.name = name
        self.country = country
        self.places = []

    def add_place(self, place):
        self.places.append(place)

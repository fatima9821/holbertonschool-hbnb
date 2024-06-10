#!/usr/bin/python3
""" create country """


class Country:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cities = []

    def add_city(self, city):
        self.cities.append(city)

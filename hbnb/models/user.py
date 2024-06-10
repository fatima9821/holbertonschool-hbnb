#!/usr/bin/python3
"""classe name """


class User:

    def __init__(self, id, email, password, first_name, last_name):
        self.id = id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.places = []
        # lutilisateur peut avoir plusieurs places

    def create_place(self, place):
        self.places.append(place)

    # Méthode d'authentification
    def authenticate(self, password):
        return self.password == password

#!/usr/bin/python3
"""classe name """
from datetime import datetime
import uuid


class User:
    _emails = set()

    def __init__(self, id, email, password, first_name, last_name):
        if email in User._emails:
            raise ValueError("Email already exists")
        User._emails.add(email)
        self.id = id or str(uuid.uuid4())
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []
        # lutilisateur peut avoir plusieurs places

    def create_place(self, place):
        self.places.append(place)

    # Méthode d'authentification
    def authenticate(self, password):
        return self.password == password

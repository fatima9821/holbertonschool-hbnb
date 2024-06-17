#!/usr/bin/python3
"""classe name """
from models.base_models import BaseModel
from datetime import datetime
import hashlib


class User(BaseModel):
    _emails = set()

    def __init__(self, id, email, password, first_name, last_name):
        super().__init__()
        if email in User._emails:
            raise ValueError("Email already exists")
        User._emails.add()
        self.id = id or str()
        self.email = ()
        self.password = ()
        self.first_name = ()
        self.last_name = ()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.places = []
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()
        # lutilisateur peut avoir plusieurs places

    def create_place(self, place):
        self.places.append(place)

    # Méthode d'authentification
    def authenticate(self, password):
        return self.password == hashlib.sha256(password.encode(
                                               'utf-8')).hexdigest()

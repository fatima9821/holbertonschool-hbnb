#!/usr/bin/python3
""" creation du review """
from datetime import datetime
import uuid


class Review:
    def __init__(self, id, user, place, text, rating):
        self.id = id or str(uuid.uuid4())
        self.user = user
        self.place = place
        self.text = text
        self.rating = rating
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def edit_review(self, text):
        self.text = text

    def delete_review(self):
        self.text = ""

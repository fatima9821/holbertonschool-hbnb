#!/usr/bin/python3
""" creation du review """
from models.base_models import BaseModel
from datetime import datetime


class Review(BaseModel):
    def __init__(self, user_id, place_id, text, rating):
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.text = text
        self.rating = rating
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def edit_review(self, text):
        self.text = text

    def delete_review(self):
        self.text = ""

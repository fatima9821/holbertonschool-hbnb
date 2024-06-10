#!/usr/bin/python3
""" creation du riview """


class Review:
    def __init__(self, id, user, place, text):
        self.id = id
        self.user = user
        self.place = place
        self.text = text

    def edit_review(self, text):
        self.text = text

    def delete_review(self):
        self.text = ""

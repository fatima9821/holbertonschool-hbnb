import pytest
from models.review import Review


def test_review_creation():
    review = Review(id="1", text="Des grands espaces!", rating=7,
                        user="Maiyra Mai", place="Belle Demeure")
    assert review.id == "1"
    assert review.text == "Des grands espaces!"
    assert review.rating == 7
    assert review.user == "Maiyra Mai"
    assert review.place == "Belle Demeure"


def test_edit_review():
     review = Review(id="1", text="Des grands espaces!", rating=7,
                     user="Maiyra Mai", place="Belle Demeure")
     review.edit_review("Updated review text")
     assert review.text == "Updated review text"


def test_delete_review():
    review = Review(id="1", text="Des grands espaces!", rating=7,
                    user="Maiyra Mai", place="Belle Demeure")
    review.delete_review()
    assert review.text == ""

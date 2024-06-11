import pytest
from unittest.mock import patch
from models.review import Review


@patch('models.review.Review.__init__', return_value=None)
def test_review_creation(mock_init):
    review = Review(id="1", text="Des grands espaces!", rating=7,
                        user="Maiyra Mai", place="Belle Demeure")
    review.__init__.assert_called_once_with(id="1",
                                             text="Des grands espaces!",
                                             rating=7,
                                             user="Maiyra Mai",
                                             place="Belle Demeure")


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

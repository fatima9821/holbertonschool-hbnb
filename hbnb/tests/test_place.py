import pytest
from unittest.mock import patch
from models.place import Place
from models.amenity import Amenity
from models.review import Review


@patch('models.place.Place.__init__', return_value=None)
def test_place_creation(mock_init):
    place = Place(
        id="1", name="Belle Demeure",
        description="un petit paradis!",
        address="Place d'Armes", city="City",
        latitude=48.801407, longitude=2.130122,
        host="Moctar Moctar", number_of_rooms=14, bathrooms=14,
        price_per_night=150, max_guests=24
    )
    place.__init__.assert_called_once_with(
        id="1", name="Belle Demeure",
        description="un petit paradis!",
        address="Place d'Armes", city="City",
        latitude=48.801407, longitude=2.130122,
        host="Moctar Moctar", number_of_rooms=14, bathrooms=14,
        price_per_night=150, max_guests=24
    )


def test_add_amenity():
    place = Place(
        id="1", name="Belle Demeure",
        description="un petit paradis!",
        address="Place d'Armes", city="City",
        latitude=48.801407, longitude=2.130122,
        host="Moctar Moctar", number_of_rooms=14, bathrooms=14,
        price_per_night=150, max_guests=24
    )
    amenity = Amenity(id="1", name="Grandes Eaux Nocturnes")
    place.add_amenity(amenity)
    assert amenity in place.amenities


def test_add_review():
    place = Place(
        id="1", name="Belle Demeure", description="un petit paradis!",
        address="Place d'Armes", city="City", latitude=48.801407,
        longitude=2.130122, host="Moctar Moctar", number_of_rooms=14,
        bathrooms=14, price_per_night=150, max_guests=24
    )
    review = Review(id="1", text="Des grands espaces!", rating=7,
                    user="Maiyra Mai", place=place)
    place.add_review(review)
    assert review in place.reviews

if __name__ == "__main__":
    pytest.main()

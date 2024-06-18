import pytest
from models.place import Place
from models.amenity import Amenity
from models.review import Review



def test_place_creation():
    place = Place(
        id="1", name="Belle Demeure",
        description="un petit paradis!",
        address="Place d'Armes", city="City",
        latitude=48.801407, longitude=2.130122,
        host="Moctar Moctar", number_of_rooms=14, bathrooms=14,
        price_per_night=150, max_guests=24
    )
    assert place.id == "1"
    assert place.name == "Belle Demeure"
    assert place.description == "un petit paradis!"
    assert place.address == "Place d'Armes"
    assert place.city == "city"
    assert place.latitude == 48.801407
    assert place.longitude == 2.130122
    assert place.host == "Moctar Moctar"
    assert place.number_of_rooms == 14
    assert place.bathrooms == 14
    assert place.price_per_night == 150
    assert place.max_guests == 24


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

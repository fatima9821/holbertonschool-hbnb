import pytest
from models.country import Country


def test_country_creation():
    country = Country(id="1", name="France")
    assert country.id == "1"
    assert country.name == "France"

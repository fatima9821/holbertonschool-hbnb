import pytest
from models.city import City


def test_city_creation():
    city = City(id="1", name="Yvelines", country="France")
    assert city.id =="1"
    assert city.name == "Yvelines"
    assert city.country == "France"

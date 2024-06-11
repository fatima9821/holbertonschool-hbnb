import pytest
from unittest.mock import patch
from models.city import City


@patch('models.city.City.__init__', return_value=None)
def test_city_creation(mock_init):
    city = City(id="1", name="Yvelines", country="France")
    city.__init__.assert_called_once_with(id="1", name="Yvelines",
                                          country="France")

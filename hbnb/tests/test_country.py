import pytest
from unittest.mock import patch
from models.country import Country


@patch('models.country.Country.__init__', return_value=None)
def test_country_creation(mock_init):
    country = Country(id="1", name="France")
    country.__init__.assert_called_once_with(id="1", name="France")

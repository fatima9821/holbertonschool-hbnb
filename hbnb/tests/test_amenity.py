import pytest
from unittest.mock import patch
from models.amenity import Amenity

@patch('models.amenity.Amenity.__init__', return_value=None)
def test_amenity_creation(mock_init):
    amenity = Amenity(id="1", name="Grandes Eaux Nocturnes")
    amenity.__init__.assert_called_once_with(id="1",
                                             name="Grandes Eaux Nocturnes")

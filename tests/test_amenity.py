import pytest
from models.amenity import Amenity


def test_amenity_creation():
    with pytest.raises(TypeError):
        amenity = Amenity(id="1", name="Grandes Eaux Nocturnes")

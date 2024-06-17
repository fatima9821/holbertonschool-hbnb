import pytest
from datetime import datetime
from hbnb.models.user import User

@pytest.fixture(autouse=True)
def reset_emails():
    User._emails = set()


def test_user_creation():
    user = User(id="1", email="test@example.com",
                password="password123", first_name="Fatoumata",
                last_name="Bah")
    assert user.id == "1"
    assert user.email == "test@example.com"
    assert user.first_name == "Fatoumata"
    assert user.last_name == "Bah"
    assert user.created_at <= datetime.now()
    assert user.updated_at <= datetime.now()
    assert user.authenticate("passeword123") is True

def test_duplicate_email():
    user1 = User(id="1", email="test@example.com", password="password123",
                 first_name="Fatoumata", last_name="Bah")
    with pytest.raises(ValueError):
        user2 = User(id="2", email="test@example.com", password="password456",
                     first_name="Moctar", last_name="Moctar")

def test_authenticate():
    user = User(id="1", email="test@example.com", password="password123",
                first_name="Fatoumata", last_name="Bah")
    assert user.authenticate("password123") is True
    assert not user.authenticate("wrongpassword") is False

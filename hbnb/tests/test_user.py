import pytest
from unittest.mock import patch
from models.user import User

@pytest.fixture(autouse=True)
def reset_emails():
    User._emails = set()

@patch('models.user.User.__init__', return_value=None)
def test_user_creation(mock_init):
    user = User(id="1", email="test@example.com",
                password="password123", first_name="Fatoumata",
                last_name="Bah")
    user.__init__.assert_called_once_with(id="1", email="test@example.com",
                                          password="password123",
                                          first_name="Fatoumata", last_name="Bah")

def test_duplicate_email():
    user1 = User(id="1", email="test@example.com", password="password123",
                 first_name="Fatoumata", last_name="Bah")
    with pytest.raises(ValueError):
        user2 = User(id="2", email="test@example.com", password="password456",
                     first_name="Moctar", last_name="Moctar")

def test_authenticate():
    user = User(id="1", email="test@example.com", password="password123",
                first_name="Fatoumata", last_name="Bah")
    assert user.authenticate("password123")
    assert not user.authenticate("wrongpassword")
    

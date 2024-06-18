import pytest
from persistence.DataManager import DataManager
from models.user import User


class TestDataManager():
    def setUp(self):
        self.manager = DataManager('test_data.json')

    def tearDown(self):
        import os
        os.remove('test_data.json')

    def test_save_user(self):
        user = User('1', 'test@example.com', 'password123', 'John', 'Doe')
        saved_user = self.manager.save(user.to_dict())
        self.assertEqual(saved_user['email'], 'test@example.com')

    def test_get_user(self):
        user = User('1', 'test@example.com', 'password123', 'John', 'Doe')
        self.manager.save(user.to_dict())
        retrieved_user = self.manager.get('1', 'User')
        self.assertEqual(retrieved_user['email'], 'test@example.com')

    def test_update_user(self):
        user = User('1', 'test@example.com', 'password123', 'John', 'Doe')
        self.manager.save(user.to_dict())
        user.first_name = 'Jane'
        updated_user = self.manager.update(user.to_dict())
        self.assertEqual(updated_user['first_name'], 'Jane')

    def test_delete_user(self):
        user = User('1', 'test@example.com', 'password123', 'John', 'Doe')
        self.manager.save(user.to_dict())
        result = self.manager.delete('1', 'User')
        self.assertTrue(result)
        self.assertIsNone(self.manager.get('1', 'User'))

if __name__ == '__main__':
    pytest.main()

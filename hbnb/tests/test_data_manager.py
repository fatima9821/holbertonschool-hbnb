import unittest
from persistance.DataManager import DataManager


class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.data_manager = DataManager('test_data.json')
        # Ensure the test data file is clean before each test
        with open('test_data.json', 'w') as f:
            json.dump({}, f)
    
    def test_save_and_get_user(self):
        user = {
            'type': 'User',
            'email': 'test@example.com',
            'password': 'password123',
            'first_name': 'Test',
            'last_name': 'User',
            'created_at': '2023-06-01T12:00:00Z',
            'updated_at': '2023-06-01T12:00:00Z'
        }
        user_id = self.data_manager.save(user)
        retrieved_user = self.data_manager.get(user_id, 'User')
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user['email'], 'test@example.com')
    
    def test_update_user(self):
        user = {
            'type': 'User',
            'email': 'yveline@gmail.com',
            'password': 'password123',
            'first_name': 'Yveline',
            'last_name': 'Mendes',
            'created_at': '2023-06-01T12:00:00Z',
            'updated_at': '2023-06-01T12:00:00Z'
        }
        user_id = self.data_manager.save(user)
        user['id'] = user_id
        user['first_name'] = 'Updated'
        self.data_manager.update(user)
        updated_user = self.data_manager.get(user_id, 'User')
        self.assertEqual(updated_user['first_name'], 'Updated')
    
    def test_delete_user(self):
        user = {
            'type': 'User',
            'email': 'fatoumata@gmail.com',
            'password': 'password123',
            'first_name': 'Bah',
            'last_name': 'Fatoumata',
            'created_at': '2023-06-01T12:00:00Z',
            'updated_at': '2023-06-01T12:00:00Z'
        }
        user_id = self.data_manager.save(user)
        self.data_manager.delete(user_id, 'User')
        deleted_user = self.data_manager.get(user_id, 'User')
        self.assertIsNone(deleted_user)

if __name__ == '__main__':
    unittest.main()


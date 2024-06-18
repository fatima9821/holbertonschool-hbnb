import unittest
import json
from api.app import app

class UserManagementTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_create_user(self):
        # Test user creation
        user_data = {
            'email': 'test@example.com',
            'first_name': 'Yveline',
            'last_name': 'Fatou'
        }
        response = self.app.post('/users', data=json.dumps(user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', json.loads(response.data))

    def test_get_all_users(self):
        # Test retrieving all users
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(json.loads(response.data), list)

    def test_get_user(self):
        # Test retrieving a specific user
        user_data = {
            'email': 'specific@example.com',
            'first_name': 'Specific',
            'last_name': 'User'
        }
        post_response = self.app.post('/users', data=json.dumps(user_data), content_type='application/json')
        user_id = json.loads(post_response.data)['id']

        get_response = self.app.get(f'/users/{user_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertIn('email', json.loads(get_response.data))
        self.assertEqual(json.loads(get_response.data)['email'], 'specific@example.com')

    def test_update_user(self):
        # Test updating a user
        user_data = {
            'email': 'update@example.com',
            'first_name': 'Update',
            'last_name': 'User'
        }
        post_response = self.app.post('/users', data=json.dumps(user_data), content_type='application/json')
        user_id = json.loads(post_response.data)['id']

        updated_data = {
            'email': 'updated@example.com',
            'first_name': 'Updated',
            'last_name': 'User'
        }
        put_response = self.app.put(f'/users/{user_id}', data=json.dumps(updated_data), content_type='application/json')
        self.assertEqual(put_response.status_code, 200)

        get_response = self.app.get(f'/users/{user_id}')
        self.assertEqual(json.loads(get_response.data)['email'], 'updated@example.com')

    def test_delete_user(self):
        # Test deleting a user
        user_data = {
            'email': 'delete@example.com',
            'first_name': 'Delete',
            'last_name': 'User'
        }
        post_response = self.app.post('/users', data=json.dumps(user_data), content_type='application/json')
        user_id = json.loads(post_response.data)['id']

        delete_response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(delete_response.status_code, 204)

        get_response = self.app.get(f'/users/{user_id}')
        self.assertEqual(get_response.status_code, 404)

if __name__ == '__main__':
    unittest.main()


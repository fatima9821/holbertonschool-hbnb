from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from hbnb.persistence.DataManager import DataManager
import re

app = Flask(__name__)
api = Api(app, version='1.0', title='User Management API', description='API for managing users')

# Initialize DataManager instance
data_manager = DataManager()

# Define data models for request input and response output
user_model = api.model('User', {
    'email': fields.String(required=True, description='User email'),
    'first_name': fields.String(required=True, description='User first name'),
    'last_name': fields.String(required=True, description='User last name'),
})

# Utility function to validate email format
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Utility function to validate non-empty strings
def validate_non_empty_string(value):
    return isinstance(value, str) and len(value.strip()) > 0

# Error handling decorator
@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.' if not str(e) else str(e)
    return {'message': message}, 500

@api.route('/users')
class UserList(Resource):
    @api.doc('list_users')
    def get(self):
        """List all users"""
        return list(data_manager.get_all()), 200

    @api.doc('create_user')
    @api.expect(user_model)
    def post(self):
        """Create a new user"""
        data = request.json
        if not validate_email(data.get('email', '')):
            return {'message': 'Invalid email format'}, 400
        if not validate_non_empty_string(data.get('first_name', '')):
            return {'message': 'First name is required'}, 400
        if not validate_non_empty_string(data.get('last_name', '')):
            return {'message': 'Last name is required'}, 400

        # Check for duplicate email
        users = data_manager.get_all()
        if any(user['email'] == data['email'] for user in users):
            return {'message': 'Email already exists'}, 409

        user_id = data_manager.save(data)
        return {'id': user_id}, 201

@api.route('/users/<string:user_id>')
class User(Resource):
    @api.doc('get_user')
    def get(self, user_id):
        """Fetch a user given its identifier"""
        user = data_manager.get(user_id)
        if user is None:
            return {'message': 'User not found'}, 404
        return user, 200

    @api.doc('update_user')
    @api.expect(user_model)
    def put(self, user_id):
        """Update a user given its identifier"""
        data = request.json
        if not validate_email(data.get('email', '')):
            return {'message': 'Invalid email format'}, 400
        if not validate_non_empty_string(data.get('first_name', '')):
            return {'message': 'First name is required'}, 400
        if not validate_non_empty_string(data.get('last_name', '')):
            return {'message': 'Last name is required'}, 400

        # Check if the user exists
        if not data_manager.get(user_id):
            return {'message': 'User not found'}, 404

        if data_manager.update(user_id, data):
            return {'message': 'User updated successfully'}, 200
        return {'message': 'Failed to update user'}, 500

    @api.doc('delete_user')
    def delete(self, user_id):
        """Delete a user given its identifier"""
        if data_manager.delete(user_id):
            return {'message': 'User deleted successfully'}, 204
        return {'message': 'User not found'}, 404

if __name__ == '__main__':
    app.run(debug=True)


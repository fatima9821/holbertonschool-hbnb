from flask import  Flask, request, jsonify, abort
from flask_restx import API, Resource, fields
from datetime import datetime
from hbnb.persistence.DataManager import DataManager


app = Flask(__name__ )
api = API(app, version='1.0', title='User Managemnt API', description='API for managing users')


#Initialize DataManager instance
DataManager = DataManager()

# Define data models for request input and response output
user_models = api.models('User', {
    'email': fields.String(required=True, description='User email'),
    'first_name': fields.String(required=True, description='User first name'),
    'last_name': fields.String(required=True, description='User last name'),
    'id': fields.string(description='User ID (generated automatically)'),
    'cerated_at': fields.DateTime(description='User creation timestamp'),
    'updated_at': fields.DateTime(description='User last update timestamp')
})

# Utility function to valide email format
def validate_email(email):
    if not isinstance(email, str) or '@' not in email:
        return False
    return True

# Utility function to validate non-empty strings
def validate_non_empty_string(value):
    if not isinstance(value, str) or len(value.strip()) == 0:
        return False
    return True

#Error handling decorator
@api.errorhandler
def default_erroe_handler(e):
    message = 'An unhandled exception occured.' if not str(e) else str(e)
    return {'message': message}, 500

""" Endpoints Implementation """

# POST /users: Create a new user
@api.route('/users')
class UserList(Resource):
    @api.expect(user_models, validate=True)
    def post(self):
        data = api.payload
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        # validate input
        if not validate_email(email):
            return {'message': 'Invalid email format'}, 400
        if not validate_non_empty_string(first_name):
            return {'message': 'First name cannot be empty'}, 400
        if not validate_non_empty_string(last_name):
            return {'message': 'Last name cannot be empty'}, 400
        
        # Chek for existing email
        existing_user = next((user for user in DataManager.get_all_users() if user['email'] == email), None)
        if existing_user:
            return {'message': 'Email already exists'}, 400
        
        # Prepare new user object
        new_user = {
            'id': None,
            'email': email,
            'first_name': last_name,
            'last_name': last_name,
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }

        # Save user to persisctence layer
        user_id = DataManager.save_user(new_user)
        new_user['id'] = user_id

        return new_user, 201
    
# GET /users: Retrieve a list of all users
@api.route('/usres')
class UserList(Resource):
    def get(self):
        users = DataManager.get_all_users()
        return users, 200
    
# GET /users/{user_id}: Retrieve details of a specific user
@api.route('/users/<string:user_id>')
class User(Resource):
    def get(self, user_id):
        user = DataManager.get_user(user_id)
        if not user:
            return {'message': 'User not found'}, 404
        return user, 200
    
# PUT /users/{user_id}: Update an existing user
@api.route('/usres/<string:user_id>')
class User(Resource):
    @api.expect(user_models, validate=True)
    def put(self, user_id):
        data = api.payload
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')

        #validate input
        if not validate_email(email):
            return {'messegae': 'Ivalid email format'}, 400
        if not validate_non_empty_string(first_name):
            return {'message': 'First name cannot be empty'}, 400
        if not validate_non_empty_string(last_name):
            return {'message': 'Last name cannot be empty'}, 400
        
        # Check if user exists
        existing_user = DataManager.get_user(user_id)
        if not existing_user:
            return {'message': 'User not found'}, 404
        
        # Update user dat
        existing_user['email'] = email
        existing_user['first_name'] = first_name
        existing_user['last_name'] = last_name
        existing_user['updated_at'] = datetime.utcnow()

        # Save updated user to persistence layer
        if DataManager.update_user(existing_user):
            return existing_user, 200
        else:
            return {'message': 'Failed to update user'}, 500
        
# DELETE /usres/{user_id}: Delete a user
@api.route('/users/<string: user_id>')
class User(Resource):
    def delete(self, user_id):
        if DataManager.delete_user(user_id):
            return '', 204
        else:
            return {'message': 'User not found'}, 404
        
""" End of Endpoints Implementation """

if __name__ == '__main__':
    app.run(debug=True)

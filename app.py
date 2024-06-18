import sys
import os

from api import app
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from models.user import User
from persistence.DataManager import DataManager
from datetime import datetime

app = Flask(__name__)
api = Api(app)
data_manager = DataManager('data.json')

class UserResource(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')

        if not email or not first_name or not last_name:
            return {'error': 'Missing required fields'}, 400

        existing_users = data_manager.data.get('User', {}).values()
        if any(user['email'] == email for user in existing_users):
            return {'error': 'Email already exists'}, 409

        user = User(email=email, first_name=first_name, last_name=last_name, password=password)
        saved_user = data_manager.save(user)
        return saved_user.to_dict(), 201

    def get(self):
        users = [User(**user_data).to_dict() for user_data in data_manager.data.get('User', {}).values()]
        return users, 200

class UserDetailResource(Resource):
    def get(self, user_id):
        user_data = data_manager.get(user_id)
        if not user_data:
            return {'error': 'User not found'}, 404
        user = User(**user_data)
        return user.to_dict(), 200

    def put(self, user_id):
        data = request.json
        user_data = data_manager.get(user_id)
        if not user_data:
            return {'error': 'User not found'}, 404

        email = data.get('email', user_data['email'])
        first_name = data.get('first_name', user_data['first_name'])
        last_name = data.get('last_name', user_data['last_name'])

        if not email or not first_name or not last_name:
            return {'error': 'Missing required fields'}, 400

        existing_users = data_manager.data.get('User', {}).values()
        if any(u['email'] == email and u['id'] != user_id for u in existing_users):
            return {'error': 'Email already exists'}, 409

        user = User(
            id=user_id,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=user_data['password'],
            created_at=user_data['created_at'],
            updated_at=datetime.now().isoformat()
        )
        updated_user = data_manager.update(user)
        return updated_user, 200

    def delete(self, user_id):
        user_data = data_manager.get(user_id)
        if not user_data:
            return {'error': 'User not found'}, 404

        data_manager.delete(user_id)
        return '', 204

api.add_resource(UserResource, '/users')
api.add_resource(UserDetailResource, '/users/<user_id>')

if __name__ == '__main__':
    app.run(debug=True)

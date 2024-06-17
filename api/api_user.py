from flask_restx import Namespace, Resource, fields
from models.user import User
from persistence.data_manager import DataManager

ns = Namespace('users', description='Operations related to users')

user_model = ns.model('User', {
    'id': fields.String(readOnly=True, description='The unique identifier of a user'),
    'email': fields.String(required=True, description='The email address of the user'),
    'first_name': fields.String(required=True, description='The first name of the user'),
    'last_name': fields.String(required=True, description='The last name of the user'),
    'password': fields.String(required=True, description='The password of the user')
})

data_manager = DataManager('data.json')

@ns.route('/')
class UserList(Resource):
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        data = ns.payload
        email = data.get('email')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        password = data.get('password')

        if not email or not first_name or not last_name or not password:
            ns.abort(400, "Missing required fields")

        existing_users = data_manager.get_all('User')
        if any(user['email'] == email for user in existing_users):
            ns.abort(409, "Email already exists")

        user = User(email=email, first_name=first_name, last_name=last_name, password=password)
        saved_user_id = data_manager.save(user.to_dict())
        saved_user = data_manager.get(saved_user_id, 'User')
        return saved_user, 201

    @ns.marshal_with(user_model)
    def get(self):
        users = data_manager.get_all('User')
        return users, 200

@ns.route('/<string:user_id>')
class UserDetail(Resource):
    @ns.marshal_with(user_model)
    def get(self, user_id):
        user_data = data_manager.get(user_id, 'User')
        if not user_data:
            ns.abort(404, "User not found")
        return user_data

    @ns.expect(user_model)
    @ns.marshal_with(user_model)
    def put(self, user_id):
        data = ns.payload
        user_data = data_manager.get(user_id, 'User')
        if not user_data:
            ns.abort(404, "User not found")

        email = data.get('email', user_data['email'])
        first_name = data.get('first_name', user_data['first_name'])
        last_name = data.get('last_name', user_data['last_name'])

        if not email or not first_name or not last_name:
            ns.abort(400, "Missing required fields")

        existing_users = data_manager.get_all('User')
        if any(u['email'] == email and u['id'] != user_id for u in existing_users):
            ns.abort(409, "Email already exists")

        user_data.update({
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'updated_at': datetime.now().isoformat()
        })

        data_manager.update(user_data)
        return user_data, 200

    def delete(self, user_id):
        user_data = data_manager.get(user_id, 'User')
        if not user_data:
            ns.abort(404, "User not found")

        data_manager.delete(user_id, 'User')
        return '', 204


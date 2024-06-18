from flask_restx import Namespace, Resource, fields
from persistence.DataManager import DataManager

api = Namespace("users", description="Users related operations")

users_model = api.model(
    "Users",
    {
        "id": fields.String(required=True, description="The user's ID"),
        "username": fields.String(required=True, description="username for user"),
        "password": fields.String(required=True, description="user password"),
        "first_name": fields.String(required=True, description="user first name"),
        "last_name": fields.String(required=True, description="user last name"),
        "email": fields.String(required=True, description="user email"),
        "age": fields.Integer(required=True, description="user age"),
    },
)

@api.route("/")
class UsersList(Resource):
    @api.doc("list_users")
    @api.marshal_list_with(users_model)
    def get(self):
        """List all users"""
        users = UsersManager().getUsers()
        if not users:
            return []
        return [user.toJSON() for user in users]

@api.route("/<string:id>")
@api.param("id", "The user identifier")
@api.response(404, "User not found")
class UsersRetrieve(Resource):
    @api.doc("get_user")
    @api.marshal_with(users_model)
    def get(self, id):
        """Fetch a user given its identifier"""
        user = UsersManager().getUser(id)
        if user:
            return user.toJSON()
        api.abort(404, "User {} doesn't exist".format(id))


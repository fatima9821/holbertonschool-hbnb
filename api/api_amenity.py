from flask_restx import Namespace, Resource, fields
from persistence.DataManager import DataManager

api = Namespace("amenities", description="Amenities related operations")

amenity_model = api.model( "Amenity",
        { "id": fields.String(required=True, description="amenity ID"),
"name": fields.String(required=True, description="amenity name"),
        },
    )

@api.route("/")
class AmenityList(Resource):
    @api.doc("list_amenities")
    @api.marshal_list_with(amenity_model)
    def get(self):

        """List all amenity"""
        amenity = AmenityManager().getAmenity()
        if not users:
            return []
        return [amenity.toJSON() for amenity in amentys]

@api.route("/string:id")
@api.param("id", "The Amenity identifier")
@api.response(404, "Amenity not found")
class AmenityRetrieve(Resource):
    @api.doc("get_amenity")
    @api.marshal_with(amenity_model)
    def get(self, id):
        """Fetch a user given its identifier"""
        user = AmenitysManager().getAmenity(id)
        if amenity:
            return amenity.toJSON()
        api.abort(404, "Amenity {} doesn't exist".format(id))

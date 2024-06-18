from flask_restful import Resource, api
from models.amenity import AmenityModel


class AmenityList(Resource):
    def get(self):
        amenities = AmenityModel.query.all()
        return {'amenities': [amenity.json() for amenity in amenities]}

    def post(self):
        data = self.get_json()
        new_amenity = AmenityModel(name=data['name'], description=data['description'])
        new_amenity.save_to_db()
        return {'message': 'Commodité créée avec succès'}, 201

class Amenity(Resource):
    def get(self, amenity_id):
        amenity = AmenityModel.query.get(amenity_id)
        if amenity is None:
            return {'message': 'Commodité introuvable'}, 404
        return {'amenity': amenity.json()}

    def put(self, amenity_id):
        data = self.get_json()
        amenity = AmenityModel.query.get(amenity_id)
        if amenity is None:
            return {'message': 'Commodité introuvable'}, 404
        amenity.name = data.get('name')
        amenity.description = data.get('description')
        amenity.update_in_db()
        return {'message': 'Commodité mise à jour avec succès'}

    def delete(self, amenity_id):
        amenity = AmenityModel.query.get(amenity_id)
        if amenity is None:
            return {'message': 'Commodité introuvable'}, 404
        amenity.delete_from_db()
        return {'message': 'Commodité supprimée avec succès'}

api = Api(None)

ns = api.namespace('', description='Opérations liées aux commodités')

ns.add_resource(AmenityList, '/')
ns.add_resource(Amenity, '/<int:amenity_id>')

from flask_restful import Resource, Api
from models.place import PlaceModel
from models.amenity import AmenityModel
from models.review import ReviewModel


class PlaceList(Resource):
    def get(self):
        places = PlaceModel.query.all()
        return {'places': [place.json() for place in places]}

    def post(self):
        data = self.get_json()
        new_place = PlaceModel(
            name=data['name'],
            description=data['description'],
            city_id=data['city_id'],
        )
        new_place.save_to_db()
        return {'message': 'Lieu créé avec succès'}, 201

class Place(Resource):
    def get(self, place_id):
        place = PlaceModel.query.get(place_id)
        if place is None:
            return {'message': 'Lieu introuvable'}, 404
        place_json = place.json()
        reviews = ReviewModel.query.filter_by(place_id=place.id).all()
        place_json['reviews'] = [review.json() for review in reviews]
        amenities = AmenityModel.query.filter_by(place_id=place.id).all()
        place_json['amenities'] = [amenity.json() for amenity in amenities]
        return {'place': place_json}

    def put(self, place_id):
        data = self.get_json()
        place = PlaceModel.query.get(place_id)
        if place is None:
            return {'message': 'Lieu introuvable'}, 404
        place.name = data.get('name')
        place.description = data.get('description')
        place.city_id = data.get('city_id')
        place.update_in_db()
        return {'message': 'Lieu mis à jour avec succès'}

    def delete(self, place_id):
        place = PlaceModel.query.get(place_id)
        if place is None:
            return {'message': 'Lieu introuvable'}, 404
        place.delete_from_db()
        return {'message': 'Lieu supprimé avec succès'}

api = Api(None)
ns = api.namespace('', description='Opérations liées aux lieux')

ns.add_resource(PlaceList, '/')
ns.add_resource(Place, '/<int:place_id>')

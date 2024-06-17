from flask_restful import Resource, Api
from models.review import ReviewModel
from models.place import PlaceModel
from flask_jwt_extended import jwt_required, get_raw_jwt

class ReviewList(Resource):
    def get(self, place_id):
        reviews = ReviewModel.query.filter_by(place_id=place_id).all()
        return {'reviews': [review.json() for review in reviews]}

    @jwt_required()
    def post(self, place_id):
        raw_jwt = get_raw_jwt()
        user_id = raw_jwt['user_id']
        data = self.get_json()
        new_review = ReviewModel(
            place_id=place_id,
            user_id=user_id,
            content=data['content'],
            rating=data['rating']
        )
        new_review.save_to_db()
        return {'message': 'Avis créé avec succès'}, 201

class Review(Resource):
    @jwt_required()
    def get(self, review_id):
        review = ReviewModel.query.get(review_id)
        if review is None:
            return {'message': 'Avis introuvable'}, 404
        return {'review': review.json()}

    @jwt_required()
    def put(self, review_id):
        data = self.get_json()
        review = ReviewModel.query.get(review_id)
        if review is None:
            return {'message': 'Avis introuvable'}, 404
        review.content = data.get('content')
        review.rating = data.get('rating')
        review.update_in_db()
        return {'message': 'Avis mis à jour avec succès'}

    @jwt_required()
    def delete(self, review_id):
        review = ReviewModel.query.get(review_id)
        if review is None:
            return {'message': 'Avis introuvable'}, 404
        review.delete_from_db()
        return {'message': 'Avis supprimé avec succès'}

api = Api(None)
ns = api.namespace('', description='Opérations liées aux avis')

ns.add_resource(ReviewList, '/places/<int:place_id>/reviews')
ns.add_resource(Review, '/reviews/<int:review_id>')

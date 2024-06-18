from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager
from model.city import City
from datetime import datetime

api = Namespace('cities', description='City related operations')
data_manager = DataManager('data.json')

city_model = api.model('City', {
    'name': fields.String(required=True, description='City name'),
    'country_id': fields.Integer(required=True, description='Country ID')
})

@api.route('/')
class CityList(Resource):
    @api.doc('list_cities')
    def get(self):
        cities = [city.json() for city in data_manager.get_all(City)]
        return {'cities': cities}, 200

    @api.expect(city_model)
    @api.doc('create_city')
    def post(self):
        data = request.json
        new_city = City(name=data['name'], country_id=data['country_id'])
        data_manager.save(new_city)
        return {'message': 'City created successfully'}, 201

@api.route('/<int:city_id>')
@api.response(404, 'City not found')
class City(Resource):
    @api.doc('get_city')
    def get(self, city_id):
        city = data_manager.get(City, city_id)
        if city is None:
            return {'message': 'City not found'}, 404
        return city.json(), 200

    @api.doc('delete_city')
    def delete(self, city_id):
        city = data_manager.get(City, city_id)
        if city is None:
            return {'message': 'City not found'}, 404
        data_manager.delete(City, city_id)
        return {'message': 'City deleted successfully'}, 204


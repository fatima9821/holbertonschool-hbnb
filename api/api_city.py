#!/usr/bin/python3

from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager
from model.city import City
from datetime import datetime


class CityList(Resource):
    def get(self):
        cities = CityModel.query.all()
        return {'cities': [city.json() for city in cities]}

    def post(self):
        data = self.get_json()
        new_city = CityModel(name=data['name'], country_id=data['country_id'])
        new_city.save_to_db()
        return {'message': 'Ville créée avec succès'}, 201

class City(Resource):
    def get(self, city_id):
        city = CityModel.query.get(city_id)
        if city is None:
            return {'message': 'Ville introuvable'}, 201

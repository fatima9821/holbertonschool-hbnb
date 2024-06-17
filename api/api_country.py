from flask import request
from flask_restx import Namespace, Resource, fields
from data_manager import DataManager
from model.country import Country
from datetime import datetime


class CountryList(Resource):
    def get(self):
        countries = CountryModel.query.all()
        return {'countries': [country.json() for country in countries]}

    def post(self):

        data = self.get_json()

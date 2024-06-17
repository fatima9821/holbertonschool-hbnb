from flask_restful import Resource, Api
from models.country import CountryModel

class CountryList(Resource):
    def get(self):
        countries = CountryModel.query.all()
        return {'countries': [country.json() for country in countries]}

    def post(self):

        data = self.get_json()

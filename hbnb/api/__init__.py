from flask import Flask, jsonify, request
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models.country import Country
import json

app = Flask(__name__)

users = {}
places = {}
reviews = {}
amenities = {}
cities = {}
countries = {}

@app.route('/users', methods=['POST'])

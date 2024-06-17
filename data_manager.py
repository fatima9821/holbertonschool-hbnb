from persistence.amenity_repository import AmenityRepository
from persistence.city_repository import CityRepository
from persistence.country_repository import CountryRepository
from persistence.place_repository import PlaceRepository
from persistence.review_repository import ReviewRepository
from persistence.user_repository import UserRepository
from model.amenity import Amenity
from model.city import City
from model.country import Country
from model.place import Place
from model.review import Review
from model.user import User

class DataManager:
    """Class to manage CRUD operations for various entities."""
    def __init__(self):
        self.place_repository = PlaceRepository()
        self.user_repository = UserRepository()
        self.review_repository = ReviewRepository()
        self.amenity_repository = AmenityRepository()
        self.country_repository = CountryRepository()
        self.city_repository = CityRepository()

    # Methods for Place
    def save_place(self, place_data):
        place = Place(
            place_data['name'],
            place_data.get('description', ''),
            place_data.get('address', ''),
            place_data.get('city_id', None),
            place_data.get('latitude', None),
            place_data.get('longitude', None),
            place_data.get('host_id', None),
            place_data.get('number_of_rooms', 0),
            place_data.get('number_of_bathrooms', 0),
            place_data.get('price_per_night', 0.0),
            place_data.get('max_guests', 0),
            place_data.get('amenity_ids', []),
            place_id=place_data['place_id'],
            created_at=place_data['created_at'],
            updated_at=place_data['updated_at']
        )
        self.place_repository.save(place)
        return place.place_id

    def get_place(self, place_id):
        return self.place_repository.get(place_id)

    def update_place(self, place_id, new_data):
        place = self.place_repository.get(place_id)
        if place:
            place.update_place_data(new_data)
            self.place_repository.update(place_id, place.to_dict())
            return True
        return False

    def delete_place(self, place_id):
        return self.place_repository.delete(place_id)

    def get_all_places(self):
        return self.place_repository.get_all()

    # Methods for User
    def save_user(self, user_data):
        user = User(user_data['username'], user_data['email'], user_data['password'])
        self.user_repository.save(user)
        return user.user_id

    def get_user(self, user_id):
        return self.user_repository.get(user_id)

    def update_user(self, user_id, new_data):
        user = self.user_repository.get(user_id)
        if user:
            user.update_user_data(new_data)
            self.user_repository.update(user_id, user.to_dict())
            return True
        return False

    def delete_user(self, user_id):
        return self.user_repository.delete(user_id)

    def get_all_users(self):
        return self.user_repository.get_all()

    # Methods for Review
    def save_review(self, review_data):
        review = Review(**review_data)
        self.review_repository.save(review)
        return review.review_id

    def get_review(self, review_id):
        return self.review_repository.get(review_id)

    def update_review(self, review_id, new_data):
        return self.review_repository.update(review_id, new_data)

    def delete_review(self, review_id):
        return self.review_repository.delete(review_id)

    def get_all_reviews(self):
        return self.review_repository.get_all()

    # Methods for Amenity
    def save_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repository.save(amenity)
        return amenity.amenity_id

    def get_amenity(self, amenity_id):
        return self.amenity_repository.get(amenity_id)

    def update_amenity(self, amenity_id, new_data):
        return self.amenity_repository.update(amenity_id, new_data)

    def delete_amenity(self, amenity_id):
        return self.amenity_repository.delete(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repository.get_all()

    # Methods for Country
    def save_country(self, country_data):
        country = Country(country_data['name'])
        self.country_repository.save(country)
        return country.country_id

    def get_country(self, country_id):
        return self.country_repository.get(country_id)

    def update_country(self, country_id, new_data):
        country = self.country_repository.get(country_id)
        if country:
            country.update_user_data(new_data)
            self.country_repository.update(country_id, country.to_dict())
            return True
        return False

    def delete_country(self, country_id):
        return self.country_repository.delete(country_id)

    def get_all_countries(self):
        return self.country_repository.get_all()

    # Methods for City
    def save_city(self, city_data):
        city = City(city_data['name'], city_data['country_id'])
        self.city_repository.save(city)
        return city.city_id

    def get_city(self, city_id):
        return self.city_repository.get(city_id)

    def update_city(self, city_id, new_data):
        city = self.city_repository.get(city_id)
        if city:
            city.update_user_data(new_data)
            self.city_repository.update(city_id, city.to_dict())
            return True
        return False

    def delete_city(self, city_id):
        return self.city_repository.delete(city_id)

    def get_all_cities(self):
        return self.city_repository.get_all()

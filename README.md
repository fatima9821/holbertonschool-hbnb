# HBnB Evolution Project: Part 1

Welcome to the HBnB Evolution project! This project is a web application modeled after AirBnB using Python and Flask. In this part, you'll be setting up the foundational elements of the application.

## Project Overview

1. **Sketching with UML**: Design the application's architecture using UML diagrams.
2. **Testing Our Logic**: Create tests for the API and business logic.
3. **Building the API**: Implement the API using Flask.
4. **File-Based Data Storage**: Store data using a file-based system (text, JSON, or XML).
5. **Packaging with Docker**: Containerize the application using Docker.

## API Structure

The API consists of three layers:
- **Services Layer**: Handles requests and responses.
- **Business Logic Layer**: Processes and decision-making.
- **Persistence Layer**: Stores data (initially file-based).

## Key Entities

- **Places**: Represents properties with attributes like name, description, address, city, etc.
- **Users**: Includes hosts and reviewers with attributes like email, password, first name, and last name.
- **Reviews**: User feedback and ratings for places.
- **Amenities**: Features of places (e.g., Wi-Fi, pools).
- **Country and City**: Represents the location hierarchy.

## Common Attributes for Entities

- **Unique ID (UUID4)**
- **Creation Date (created_at)**
- **Update Date (updated_at)**

## Endpoints

### User Management

- **POST /users**: Create a new user.
- **GET /users**: Retrieve a list of all users.
- **GET /users/{user_id}**: Retrieve details of a specific user.
- **PUT /users/{user_id}**: Update an existing user.
- **DELETE /users/{user_id}**: Delete a user.

### Country and City Management

- **GET /countries**: Retrieve all countries.
- **GET /countries/{country_code}**: Retrieve details of a specific country.
- **GET /countries/{country_code}/cities**: Retrieve all cities in a country.
- **POST /cities**: Create a new city.
- **GET /cities**: Retrieve all cities.
- **GET /cities/{city_id}**: Retrieve details of a specific city.
- **PUT /cities/{city_id}**: Update a city.
- **DELETE /cities/{city_id}**: Delete a city.

### Amenity Management

- **POST /amenities**: Create a new amenity.
- **GET /amenities**: Retrieve a list of all amenities.
- **GET /amenities/{amenity_id}**: Retrieve details of a specific amenity.
- **PUT /amenities/{amenity_id}**: Update an amenity.
- **DELETE /amenities/{amenity_id}**: Delete an amenity.

### Places Management

- **POST /places**: Create a new place.
- **GET /places**: Retrieve a list of all places.
- **GET /places/{place_id}**: Retrieve details of a specific place.
- **PUT /places/{place_id}**: Update a place.
- **DELETE /places/{place_id}**: Delete a place.

### Review Management

- **POST /places/{place_id}/reviews**: Create a review for a place.
- **GET /users/{user_id}/reviews**: Retrieve all reviews by a user.
- **GET /places/{place_id}/reviews**: Retrieve all reviews for a place.
- **GET /reviews/{review_id}**: Retrieve details of a specific review.
- **PUT /reviews/{review_id}**: Update a review.
- **DELETE /reviews/{review_id}**: Delete a review.

## Containerization with Docker

### Dockerfile

1. Use Alpine Linux base image with Python.
2. Copy the application source code into the container.
3. Install dependencies using `requirements.txt`.
4. Configure Gunicorn to serve the application.
5. Set environment variables for configuration.
6. Define a volume for persistent data storage.

### Commands

- **Build the image**: `docker build -t holbertonschool-hbnb .`
- **Run the container**: `docker run -p 5000:5000 -v /host/path:/container/path holbertonschool-hbnb`

## Testing

- Write unit tests for each endpoint.
- To run the tests, use `pytest`
- Ensure data validation and error handling.
- Use Flask-Restx for API documentation.

## Documentation

- Use Flask-Restx for documenting endpoints.
- Include request/response examples and error messages.

## Repository

- GitHub repository: `https://github.com/fatima9821/holbertonschool-hbnb

## diagramme UML

![UML Diagram](https://drive.google.com/file/d/1Rqv0xq_N_2l0SdWImEEbcVhWLzVIMbed/view?usp=sharing)

## Authors
- **MOCTAR Moctar**
- **Fatoumata Bah**
- **Yveline Mendes**


## TESTS CODE

## *Hints for testing*

Here’s a set of guidelines and test cases for evaluating the models corresponding to entities like Users, Places, Reviews, Amenities, and Location Management.

- **Consistency Checks** - Across all models, test that the created_at and updated_at fields are automatically set on creation and update operations.
- **Relationship Integrity** - Test the integrity of relationships between objects, such as places to their host users and reviews to their corresponding places and users.
- **Business Rule Enforcement** - Each model test should include checks for business rule enforcement, such as one host per place, user uniqueness, and review restrictions.
- **User Creation Validation** - Test instantiation of a User object with valid and invalid inputs to verify constraints (e.g., email format, required fields).
- **Unique Email Constraint** - Attempt to create multiple users with the same email and ensure the model throws an exception or handles it as per the business rule.
- **Update Mechanism** - Verify that updates to a user’s attributes (e.g., name) are reflected in existing instances of the user.
- **Place Instantiation** - Test creating a Place object with all required fields and validate that missing or incorrect fields are handled correctly.
- **Host Assignment Rules**- Ensure that a Place object can be assigned only one host and validate that re-assignment is handled according to specified rules.
- **Place Attribute Validation** - Validate geographical coordinates (latitude and longitude) and other properties like price per night and max guests to check they are within acceptable ranges.
- **Deleting Places** - Test that when a Place is deleted, it’s removed correctly and cleans up all associated references, such as from the host’s list of places.
- **Amenity Addition** - Test adding amenities to a place, verifying that duplicates cannot be added to the same place.
- **Retrieve and Update Amenities** - Check retrieval mechanisms for amenities and ensure updates to amenity details propagate correctly.

*This is not an exhaustive list, be sure to add all the tests necessary to validate your application functionality.*

These tests should be written using a unit testing framework like unittest or pytest in Python. You should mock dependencies and focus on testing the logic within the models to ensure that all operations behave as expected without relying on the database or external systems.

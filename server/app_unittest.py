import unittest
import json
from app import app, client
from bson.objectid import ObjectId


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = client['hmo']
        self.users = self.db['users']
        self.user_id = str(ObjectId())

    def tearDown(self):
        # Clean up after each test if needed
        self.users.delete_many({})

    def test_get_all_users(self):
        # Add test for retrieving all users
        user_data = [
            {
                "id": "345",
                "first_name": "John",
                "last_name": "Smith",
                "email": "johns@example.com",
                "city": "New York",
                "street": "123 Main St",
                "building_number": "1A",
                "birth_date": "1990-01-01",
                "phone_number": "1234567890"
            },
            {
                "id": "234",
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jane@example.com",
                "city": "Los Angeles",
                "street": "456 Elm St",
                "building_number": "2B",
                "birth_date": "1992-02-02",
                "phone_number": "0987654321"
            }
        ]
        # Insert sample users into the database
        self.users.insert_many(user_data)

        # Send GET request to retrieve all users
        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)

        # Parse response data and check if both inserted users are present
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(len(data), 2)  # Assuming there are exactly two users
        # Assuming data is a list of dictionaries with user information
        self.assertIn(user_data[0], data)
        self.assertIn(user_data[1], data)

    def test_post_user(self):
        user_data = {
            "id": "123",
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "city": "New York",
            "street": "123 Main St",
            "building_number": "1A",
            "birth_date": "1990-01-01",
            "phone_number": "1234567890"
        }
        response = self.app.post('/users', json=user_data)
        self.assertEqual(response.status_code, 200)
        # data = json.loads(response.get_data(as_text=True))
        # self.assertEqual(data['id'], "123")

    def test_get_user(self):
        user_data = {
            "id": self.user_id,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "city": "New York",
            "street": "123 Main St",
            "building_number": "1A",
            "birth_date": "1990-01-01",
            "phone_number": "1234567890"
        }
        self.users.insert_one(user_data)
        response = self.app.get(f'/users/{self.user_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['id'], self.user_id)

    def test_update_user(self):
        user_data = {
            "id": self.user_id,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "city": "New York",
            "street": "123 Main St",
            "building_number": "1A",
            "birth_date": "1990-01-01",
            "phone_number": "1234567890"
        }
        self.users.insert_one(user_data)
        updated_data = {"first_name": "Jane"}
        response = self.app.put(f'/users/{self.user_id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], 'Item updated')

    def test_delete_user(self):
        user_data = {
            "id": self.user_id,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "city": "New York",
            "street": "123 Main St",
            "building_number": "1A",
            "birth_date": "1990-01-01",
            "phone_number": "1234567890"
        }
        self.users.insert_one(user_data)
        response = self.app.delete(f'/users/{self.user_id}')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['message'], 'Item deleted')


if __name__ == '__main__':
    unittest.main()


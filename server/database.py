from datetime import datetime

from pymongo import MongoClient
from pymongo.errors import OperationFailure

from models import schema

# Connect to MongoDB
uri = "mongodb+srv://tamar_31:mDw5G2Y3Arx164bN@cluster0.ica1qev.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&authSource=admin"
client = MongoClient(uri)
client.admin.command('ping')

db = client['hmo']
users = db['users']

# schema validator to users
db.command("collMod", users.name, validator=schema)

try:
    valid_user = {
        "id": "123",
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane@example.com",
        "city": "New York",
        "street": "Main Road",
        "building_number": "13",
        "birth_date": datetime(1990, 5, 15),
        "phone_number": "1234567890",
        "mobile_phone_number": "0987654321",
        "vaccines": [
            {
                "date_taken": datetime(2021, 3, 1),
                "provider": "Pfizer"
            },
            {
                "date_taken": datetime(2021, 4, 1),
                "provider": "Moderna"
            }
        ],
        "covid_positive_date": datetime(2020, 11, 1),
        "covid_recovery_date": datetime(2020, 11, 15)
    }
    users.insert_one(valid_user)
    print("Valid user document inserted successfully.")
except Exception as e:
    print(f"Error inserting valid user document: {e}")

# Test inserting an invalid user document
try:
    invalid_user = {
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "invalid_email",  # Invalid email format
        "city": "London",
        "street": "High Street",
        "building_number": "456",
        "birth_date": datetime(1985, 8, 20),
        "phone_number": "9876543210"
    }
    users.insert_one(invalid_user)
    print("Invalid user document inserted successfully.")
except OperationFailure as e:
    print(f"Error inserting invalid user document: {e}")

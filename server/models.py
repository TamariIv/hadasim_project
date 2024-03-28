schema = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": [
            "id",
            "first_name",
            "last_name",
            "email",
            "city",
            "street",
            "building_number",
            "birth_date",
            "phone_number",
            "mobile_phone_number",
            "vaccines",
            "covid_positive_date",
            "covid_recovery_date"
        ],
        "properties": {
            "id": {
                "bsonType": "string",
                "description": "must be a unique string and is required"
            },
            "first_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "last_name": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "email": {
                "bsonType": "string",
                "pattern": "^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$",
                "description": "must be a valid email address and is required"
            },
            "city": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "street": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "building_number": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "birth_date": {
                "bsonType": "string",
                "description": "must be a date string and is required"
            },
            "phone_number": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "mobile_phone_number": {
                "bsonType": "string",
                "description": "must be a string and is required"
            },
            "vaccines": {
                "bsonType": "array",
                "maxItems": 4,
                "description": "must be an array of objects and is required",
                "items": {
                    "bsonType": "object",
                    "required": [
                        "date_taken",
                        "provider"
                    ],
                    "properties": {
                        "date_taken": {
                            "bsonType": "string",
                            "description": "must be a date string and is required"
                        },
                        "provider": {
                            "bsonType": "string",
                            "description": "must be a string and is required"
                        }
                    }
                }
            },
            "covid_positive_date": {
                "bsonType": "string",
                "description": "must be a date string and is required"
            },
            "covid_recovery_date": {
                "bsonType": "string",
                "description": "must be a date string and is required"
            }
        }
    }
}

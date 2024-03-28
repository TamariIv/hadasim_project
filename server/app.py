# server/app.py

from flask import Flask, Response, request, jsonify
from pymongo import MongoClient
from flask_restful import Api, Resource
from flask_cors import CORS
import traceback

from models import schema
from tokens import MONGODB_USER, MONGODB_PASS

# Connect to MongoDB
uri = f"mongodb+srv://{MONGODB_USER}:{MONGODB_PASS}@cluster0.ica1qev.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&authSource=admin"
client = MongoClient(uri)
print(client.admin.command('ping'))

db = client['hmo']
users = db['users']

# schema validator to users
db.command("collMod", users.name, validator=schema)

app = Flask(__name__)
api = Api(app)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


class UsersApi(Resource):
    def get(self):
        # Read users
        print("in users/get")
        items = list(users.find({}, {'_id': 0}))
        return jsonify(items)

    def post(self):
        # Create a new user
        print("in users/post")
        try:
            body = request.get_json()
            print(body)
            user_id = users.insert_one(body).inserted_id
            return {'id': str(user_id)}, 201
        except Exception as e:
            print(e)
            traceback.print_exc()


class UserApi(Resource):
    def get(self, item_id):
        # Read a single user
        print("in user/get")
        try:
            item = users.find_one({'_id': item_id}, {'_id': 0})
            return jsonify(item)
        except Exception as e:
            print(e)

    def put(self, item_id):
        # Update a user
        print("in user/put")
        body = request.get_json()
        result = users.update_one({'_id': item_id}, {'$set': body})
        if result.modified_count == 1:
            return jsonify({'message': 'Item updated'})
        else:
            return jsonify({'message': 'Item not found'}), 404

    def delete(self, item_id):
        # Delete a user
        print("in user/delete")
        result = users.delete_one({'_id': item_id})
        result = users.delete_one({'_id': item_id})
        if result.deleted_count == 1:
            return jsonify({'message': 'Item deleted'})
        else:
            return jsonify({'message': 'Item not found'}), 404


api.add_resource(UsersApi, '/users')
api.add_resource(UserApi, '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

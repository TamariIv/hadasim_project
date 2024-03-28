# server/app.py

import json
from datetime import datetime

from flask import Flask, Response, request, jsonify
from pymongo import MongoClient
from flask_restful import Api, Resource
from flask_cors import CORS
import traceback

from models import schema

# Connect to MongoDB
uri = "mongodb+srv://tamar_31:mDw5G2Y3Arx164bN@cluster0.ica1qev.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0&authSource=admin"
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
        print("in users/get")
        # Read users
        items = list(users.find({}, {'_id': 0}))
        # return Response(items, mimetype="application/json", status=200)
        return jsonify(items)

    def post(self):
        print("in users/post")
        try:
            body = request.get_json()
            print(body)
            # # Convert date strings to BSON date objects
            # body['birth_date'] = datetime.strptime(body['birth_date'], '%Y-%m-%d')
            # for vaccine in body['vaccines']:
            #     vaccine['date_taken'] = datetime.strptime(vaccine['date_taken'], '%Y-%m-%d')
            # if 'covid_positive_date' in body and body['covid_positive_date'] != '':
            #     body['covid_positive_date'] = datetime.strptime(body['covid_positive_date'], '%Y-%m-%d')
            # if 'covid_recovery_date' in body and body['covid_recovery_date'] != '':
            #     body['covid_recovery_date'] = datetime.strptime(body['covid_recovery_date'], '%Y-%m-%d')

            user_id = users.insert_one(body).inserted_id
            # id = user.id
            return {'id': str(user_id)}, 201
        except Exception as e:
            print(e)
            traceback.print_exc()

        # # Create a new user
        # data = request.get_json()
        # item_id = users.insert_one(data).inserted_id
        # return jsonify({'id': str(item_id)})


class UserApi(Resource):
    def get(self, item_id):
        print("in user/get")
        try:
            item = users.find_one({'_id': item_id}, {'_id': 0})
            return Response(item, mimetype="application/json", status=200)
        except Exception as e:
            print(e)

        # Read a single user
        # item = users.find_one({'_id': item_id}, {'_id': 0})
        # if item:
        #     return jsonify(item)
        # else:
        #     return jsonify({'message': 'Item not found'}), 404

    def put(self, item_id):
        print("in user/put")
        body = request.get_json()
        result = users.update_one({'_id': item_id}, {'$set': body})
        return '', 200

        # Update a user
        # data = request.get_json()
        # result = users.update_one({'_id': item_id}, {'$set': data})
        # if result.modified_count == 1:
        #     return jsonify({'message': 'Item updated'})
        # else:
        #     return jsonify({'message': 'Item not found'}), 404

    def delete(self, item_id):
        print("in user/delete")
        result = users.delete_one({'_id': item_id})
        return '', 200

        # Delete a user
        # result = users.delete_one({'_id': item_id})
        # if result.deleted_count == 1:
        #     return jsonify({'message': 'Item deleted'})
        # else:
        #     return jsonify({'message': 'Item not found'}), 404


api.add_resource(UsersApi, '/users')
api.add_resource(UserApi, '/users/<id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

#app.py

import os
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Bird

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact=False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Birds(Resource):
    def get(self):
        birds = Bird.query.all()

        bird_dict = [bird.to_dict for bird in birds]

        response = make_response(
            jsonify(bird_dict), 200
        )

        return response

api.add_resource(Birds, '/birds')
    
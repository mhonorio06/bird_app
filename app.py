#app.py

import os

from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Bird

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Birds(Resource):

    def get(self):
        birds = [bird.to_dict() for bird in Bird.query.all()]
        return make_response(jsonify(birds), 200)

api.add_resource(Birds, '/birds')

class BirdByID(Resource):
    def get(self, id):
        bird = Bird.query.filter(Bird.id == id).first()

        bird_dict = bird.to_dict()

        response = make_response(
            jsonify(bird_dict), 200
        )

        return response
    
api.add_resource(BirdByID, '/birds/<int:id>')

# PGPASSWORD=RDRuwCl8dI7Nok7VkK156vMEXCo8HPdl pg_dump -h dpg-crpuhrd6l47c73aq8du0-a.oregon-postgres.render.com -U mhonorio06 --format=custom --no-acl --no-owner bird_app_cque > bird_app_cque.sql

# PGPASSWORD=mOONbYfUxm4rV6lPppdykgzqsWYCs72C pg_restore -h dpg-crr2av88fa8c739fsfm0-a.oregon-postgres.render.com -U mhonorio06 --verbose --clean --no-acl --no-owner -d bird_app_cque bird_app_cque.sql
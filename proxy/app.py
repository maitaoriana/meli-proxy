from flask import Flask, request, abort
from requests import get
from http import HTTPStatus
from flask_restful import Api
from database.db import initialize_db
from database.models import Clients
from resources.routes import initialize_routes
from resources.errors import errors


app = Flask(__name__)
api = Api(app, errors=errors)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://mongodb-meli/proxy'
}




initialize_db(app)
initialize_routes(api)

app.run(host="0.0.0.0", port=5000)

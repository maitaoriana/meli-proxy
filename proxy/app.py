from flask import Flask
from flask_restful import Api
from prometheus_flask_exporter import PrometheusMetrics

from database.db import initialize_db
from resources.errors import errors
from resources.routes import initialize_routes


app = Flask(__name__)
metrics = PrometheusMetrics(app)
api = Api(app, errors=errors)

app.config["MONGODB_SETTINGS"] = {"host": "mongodb://meli-mongodb/proxy"}

initialize_db(app)
initialize_routes(api)

app.run(host="0.0.0.0", port=5000)

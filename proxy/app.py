from flask import Flask, request, abort
from requests import get
from http import HTTPStatus
from flask_restful import Api
from database.db import initialize_db
from database.models import Clients
from resources.routes import initialize_routes
from resources.errors import errors

MELI_URL = 'https://api.mercadolibre.com/'

app = Flask(__name__)
api = Api(app, errors=errors)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://mongodb-meli/proxy'
}


@app.route('/', defaults={'url': ''})
@app.route('/<path:url>')
def proxy(url):
    ip = request.remote_addr
    client = Clients.objects(ip=ip).first()
    if not client or client.cant_request >= client.max_request:
        abort(HTTPStatus.UNAUTHORIZED, description="Sin autorizacion")
    client.update(inc__cant_request=1)
    return get(f'{MELI_URL}{url}').content


initialize_db(app)
initialize_routes(api)

app.run(host="0.0.0.0", port=5000)

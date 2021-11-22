from flask import Flask, request, Response, abort
from requests import get
from http import HTTPStatus
from database.db import initialize_db
from database.models import Clients

MELI_URL = 'https://api.mercadolibre.com/'

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://mongodb-meli/proxy'
}

initialize_db(app)


@app.route('/', defaults={'url': ''})
@app.route('/<path:url>')
def proxy(url):
    ip = request.remote_addr
    client = Clients.objects(ip=ip).first()
    if not client or client.cant_request >= client.max_request:
        abort(HTTPStatus.UNAUTHORIZED, description="Sin autorizacion")
    client.update(inc__cant_request=1)
    return get(f'{MELI_URL}{url}').content


@app.route('/clients')
def get_clients():
    clients = Clients.objects().to_json()
    return Response(clients, mimetype="application/json", status=200)


@app.route('/clients', methods=['POST'])
def add_clients():
    body = request.get_json()
    client = Clients(**body).save()
    return {'id': str(client.id)}, 200


@app.route('/clients/<ip>', methods=['PUT'])
def update_movie(ip):
    body = request.get_json()
    Clients.objects.get(ip=ip).update(**body)
    return '', 200

@app.route('/clients/<ip>', methods=['DELETE'])
def delete_movie(ip):
    client = Clients.objects.get(ip=ip).delete()
    return '', 200


app.run(host="0.0.0.0", port=5000)

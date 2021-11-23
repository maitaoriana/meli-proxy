from flask import Response, request
from database.models import Clients
from flask_restful import Resource


class ClientsResource(Resource):

    def get(self):
        clients = Clients.objects().to_json()
        return Response(clients, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        client = Clients(**body).save()
        return {'id': str(client.id)}, 200


class ClientResource(Resource):

    def put(self, ip):
        body = request.get_json()
        Clients.objects.get(ip=ip).update(**body)
        return '', 200

    def delete_movie(self, ip):
        client = Clients.objects.get(ip=ip).delete()
        return '', 200

    def get(self, ip):
        client = Clients.objects.get(ip=ip).to_json()
        return Response(client, mimetype="application/json", status=200)




from flask import Response, request
from flask_restful import Resource
from database.models import Clients
from mongoengine.errors import FieldDoesNotExist,NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from .errors import SchemaValidationError, IPAlreadyExistsError, NotFound


class ClientsResource(Resource):

    def get(self):
        clients = Clients.objects().to_json()
        return Response(clients, mimetype="application/json", status=200)

    def post(self):
        try:
            body = request.get_json()
            client = Clients(**body).save()
            return {'id': str(client.id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise IPAlreadyExistsError


class ClientResource(Resource):

    def put(self, ip):
        try:
            body = request.get_json()
            Clients.objects.get(ip=ip).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise NotFound

    def delete_movie(self, ip):
        try:
            client = Clients.objects.get(ip=ip).delete()
            return '', 200
        except DoesNotExist:
            raise NotFound

    def get(self, ip):
        try:
            client = Clients.objects.get(ip=ip).to_json()
            return Response(client, mimetype="application/json", status=200)
        except DoesNotExist:
            raise NotFound




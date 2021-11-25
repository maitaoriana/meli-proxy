from flask import Response, request
from flask_restful import Resource
from http import HTTPStatus
from database.models import Clients, PathRules
from mongoengine.errors import FieldDoesNotExist,NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from .errors import SchemaValidationError, IPAlreadyExistsError, NotFound


class ClientsResource(Resource):

    def get(self):
        clients = Clients.objects().to_json()
        return Response(clients, mimetype="application/json", status=HTTPStatus.OK)

    def post(self):
        try:
            body = request.get_json()
            client = Clients(**body).save()
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise IPAlreadyExistsError

        return {'id': str(client.id)}, HTTPStatus.CREATED


class ClientResource(Resource):

    def put(self, ip):
        try:
            body = request.get_json()
            client = Clients.objects.get(ip=ip)
            client.update(**body)
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise NotFound

        return {'ip': client.ip}, HTTPStatus.OK

    def delete(self, ip):
        try:
            Clients.objects.get(ip=ip).delete()
        except DoesNotExist:
            raise NotFound

        return {'status': HTTPStatus.OK}, HTTPStatus.OK

    def get(self, ip):
        try:
            client = Clients.objects.get(ip=ip).to_json()
        except DoesNotExist:
            raise NotFound

        return Response(client, mimetype="application/json", status=HTTPStatus.OK)


class ClientsResetResource(Resource):

    def get(self):
        clients = Clients.objects()
        clients.update(cant_request=0)
        for client in clients:
            client.rules.update(cant_request=0)
            client.save()
        return {'message': 'Los contadores fueron reiniciados'}, HTTPStatus.OK



from http import HTTPStatus

from flask import request
from flask import Response
from flask_restful import Resource
from mongoengine.errors import DoesNotExist
from mongoengine.errors import FieldDoesNotExist
from mongoengine.errors import InvalidQueryError
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError

from .errors import IPAlreadyExistsError
from .errors import NotFound
from .errors import SchemaValidationError
from database.models import Clients


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

        return {"id": str(client.id)}, HTTPStatus.CREATED


class ClientResource(Resource):
    def put(self, id):
        try:
            body = request.get_json()
            client = Clients.objects.get(id=id)
            client.update(**body)
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise NotFound

        return {"id": str(client.id)}, HTTPStatus.OK

    def delete(self, id):
        try:
            Clients.objects.get(id=id).delete()
        except DoesNotExist:
            raise NotFound

        return {"status": HTTPStatus.OK}, HTTPStatus.OK

    def get(self, id):
        try:
            client = Clients.objects.get(id=id).to_json()
        except DoesNotExist:
            raise NotFound
        except ValidationError:
            raise SchemaValidationError

        return Response(client, mimetype="application/json", status=HTTPStatus.OK)


class ClientsResetResource(Resource):
    def get(self):
        clients = Clients.objects()
        clients.update(cant_request=0)
        for client in clients:
            client.rules.update(cant_request=0)
            client.save()
        return {"message": "Los contadores fueron reiniciados"}, HTTPStatus.OK

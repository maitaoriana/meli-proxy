from flask import Response, request
from flask_restful import Resource
from database.models import Clients, PathRules
from mongoengine.errors import FieldDoesNotExist,NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from .errors import SchemaValidationError, IPAlreadyExistsError, NotFound


class ClientsPathRulesResource(Resource):

    def post(self, ip):
        try:
            client = Clients.objects.get(ip=ip)
            body = request.get_json()
            rule = PathRules(**body)
            client.rules.append(rule)
            client.save()
            return {'id': str(client.id)}, 201
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise IPAlreadyExistsError
        except DoesNotExist:
            raise NotFound

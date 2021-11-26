from flask import Response, request
from flask_restful import Resource
from database.models import Clients, PathRules
from mongoengine.errors import FieldDoesNotExist,NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from .errors import SchemaValidationError, IPAlreadyExistsError, NotFound
from http import HTTPStatus


class ClientsPathRulesResource(Resource):

    def post(self, client_id):
        try:
            client = Clients.objects.get(id=client_id)
            body = request.get_json()
            rule = PathRules(**body)
            client.rules.append(rule)
            client.save()
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise IPAlreadyExistsError
        except DoesNotExist:
            raise NotFound

        return {'id': str(rule.oid)}, HTTPStatus.CREATED


class ClientsPathRuleResource(Resource):

    def patch(self, client_id, rule_id):
        try:
            data = request.get_json()
            client = Clients.objects.get(id=client_id)
            client.rules.filter(oid=rule_id).update(**data)
            client.save()
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise IPAlreadyExistsError
        except DoesNotExist:
            raise NotFound

        return {'id': rule_id}, HTTPStatus.PARTIAL_CONTENT

    def delete(self, client_id, rule_id):
        try:
            client = Clients.objects.get(id=client_id)
            client.rules.filter(oid=rule_id).delete()
            client.save()
        except DoesNotExist:
            raise NotFound

        return {'status': HTTPStatus.OK}, HTTPStatus.OK

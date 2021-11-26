from flask import request
from flask_restful import Resource
from requests import get

from .errors import TooManyRequestPath
from .errors import TooManyRequests
from .errors import UnauthorizedError
from database.models import Clients

MELI_URL = "https://api.mercadolibre.com/"


class Proxy(Resource):
    def get(self, url=""):
        return self.handling_request(url)

    def inc_counter(self, client, rule=False):
        client.cant_request = client.cant_request + 1
        if rule:
            rule.cant_request = rule.cant_request + 1
        client.save()

    def validate_access(self):
        ip_client = request.remote_addr
        client = Clients.objects(ip=ip_client).first()
        path = request.path
        if not client:
            raise UnauthorizedError
        if client.cant_request >= client.max_request:
            raise TooManyRequests

        rule = client.rules.filter(path=path).first()
        if not rule:
            self.inc_counter(client)
            return True

        if rule.cant_request >= rule.max_request:
            raise TooManyRequestPath

        self.inc_counter(client, rule)
        return True

    def handling_request(self, url=""):
        self.validate_access()
        token = request.headers.get("Authorization")
        header = {"Authorization": f"{token}"} if token else {}
        response = get(f"{MELI_URL}{request.full_path}", headers=header)
        return response.json(), response.status_code


class ProxyHome(Proxy):
    def get(self):
        return self.handling_request()

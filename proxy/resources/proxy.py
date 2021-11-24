from flask import request
from flask_restful import Resource
from database.models import Clients
from requests import get
from .errors import UnauthorizedError, TooManyRequests, TooManyRequestPath

MELI_URL = 'https://api.mercadolibre.com/'


class Proxy(Resource):

    def get(self, url=""):
        ip = request.remote_addr
        return self.handling_request(ip, url)

    def handling_request(self, ip, url=""):
        client = Clients.objects(ip=ip).first()
        if not client:
            raise UnauthorizedError
        if client.cant_request >= client.max_request:
            raise TooManyRequests

        rule = client.rules.filter(path=request.path).first()
        if not rule:
            client.cant_request = client.cant_request + 1
            client.save()
            return get(f'{MELI_URL}{url}').json()

        if rule.cant_request >= rule.max_request:
            raise TooManyRequestPath

        client.cant_request = client.cant_request + 1
        rule.cant_request = rule.cant_request + 1
        client.save()
        return get(f'{MELI_URL}{url}').json()


class ProxyHome(Proxy):

    def get(self):
        return self.handling_request(request.remote_addr)

from .clients import ClientsResource,ClientResource
from .proxy import Proxy, ProxyHome


def initialize_routes(api):
    api.add_resource(ClientsResource, '/clients')
    api.add_resource(ClientResource, '/clients/<ip>')
    api.add_resource(Proxy, '/<url>')
    api.add_resource(ProxyHome, '/')

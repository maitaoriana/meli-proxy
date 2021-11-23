from .clients import ClientsResource,ClientResource


def initialize_routes(api):
    api.add_resource(ClientsResource, '/clients')
    api.add_resource(ClientResource, '/clients/<ip>')

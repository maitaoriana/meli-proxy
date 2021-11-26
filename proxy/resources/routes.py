from .clients import ClientsResource,ClientResource, ClientsResetResource
from .proxy import Proxy, ProxyHome
from .clients_path_rules import ClientsPathRulesResource, ClientsPathRuleResource


def initialize_routes(api):
    api.add_resource(ClientsPathRuleResource, '/clients/<client_id>/rules/<rule_id>')
    api.add_resource(ClientsPathRulesResource, '/clients/<client_id>/rules')
    api.add_resource(ClientResource, '/clients/<id>')
    api.add_resource(ClientsResetResource, '/clients/reset')
    api.add_resource(ClientsResource, '/clients')
    api.add_resource(Proxy, '/<path:url>')
    api.add_resource(ProxyHome, '/')

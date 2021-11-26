from .clients import ClientResource
from .clients import ClientsResetResource
from .clients import ClientsResource
from .clients_path_rules import ClientsPathRuleResource
from .clients_path_rules import ClientsPathRulesResource
from .proxy import Proxy
from .proxy import ProxyHome


def initialize_routes(api):
    api.add_resource(ClientsPathRuleResource, "/clients/<client_id>/rules/<rule_id>")
    api.add_resource(ClientsPathRulesResource, "/clients/<client_id>/rules")
    api.add_resource(ClientResource, "/clients/<id>")
    api.add_resource(ClientsResetResource, "/clients/reset")
    api.add_resource(ClientsResource, "/clients")
    api.add_resource(Proxy, "/<path:url>")
    api.add_resource(ProxyHome, "/")

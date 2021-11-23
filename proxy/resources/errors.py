

class UnauthorizedError(Exception):
    pass


class SchemaValidationError(Exception):
    pass


class PathUnauthorized(Exception):
    pass


class TooManyRequests(Exception):
    pass


class TooManyRequestPath(Exception):
    pass


class IPAlreadyExistsError(Exception):
    pass


class NotFound(Exception):
    pass


errors = {
    "UnauthorizedError": {"message": "Sin autorización", "status": 401},
    "PathUnauthorized": {"message": "No esta autorizado para acceder a esta url", "status": 401},
    "TooManyRequests": {"message": "Excedió su limite de solicitudes a la api de mercadolibre", "status": 429},
    "TooManyRequestPath": {"message": "Excedió el número de solicitudes a esta url", "status": 429},
    "IPAlreadyExistsError": {"message": "Este cliente ya existe", "status": 400},
    "SchemaValidationError": { "message": "Faltan campos requeridos", "status": 400},
    "NotFound": {"message": "El elemento no existe", "status": 404}
}

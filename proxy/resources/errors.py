from http import HTTPStatus


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
    "UnauthorizedError": {
        "message": "Sin autorización",
        "status": HTTPStatus.UNAUTHORIZED,
    },
    "PathUnauthorized": {
        "message": "No esta autorizado para acceder a esta url",
        "status": HTTPStatus.UNAUTHORIZED,
    },
    "TooManyRequests": {
        "message": "Excedió su limite de solicitudes a la api de mercadolibre",
        "status": HTTPStatus.TOO_MANY_REQUESTS,
    },
    "TooManyRequestPath": {
        "message": "Excedió el número de solicitudes a esta url",
        "status": HTTPStatus.TOO_MANY_REQUESTS,
    },
    "IPAlreadyExistsError": {
        "message": "Este cliente ya existe",
        "status": HTTPStatus.BAD_REQUEST,
    },
    "SchemaValidationError": {
        "message": "Faltan campos requeridos",
        "status": HTTPStatus.BAD_REQUEST,
    },
    "NotFound": {
        "message": "El elemento no existe",
        "status": HTTPStatus.NOT_FOUND,
    },
}

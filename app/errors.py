from dataclasses import dataclass
from http import HTTPStatus
from apiflask import HTTPError


# 204
@dataclass
class NoContentError(HTTPError):
    message: dict
    status_code: int = HTTPStatus.NO_CONTENT


# 400
@dataclass
class DomainError(HTTPError):
    message: dict
    status_code: int = HTTPStatus.BAD_REQUEST


# 401
@dataclass
class UnauthorizedError(HTTPError):
    message: dict
    status_code: int = HTTPStatus.UNAUTHORIZED


# 403
@dataclass
class ForbiddenError(HTTPError):
    message: dict
    status_code: int = HTTPStatus.FORBIDDEN


# 404
@dataclass
class NotFoundError(HTTPError):
    message: dict
    status_code: int = HTTPStatus.NOT_FOUND


# 406
@dataclass
class NotAceeptableError(HTTPError):
    message: dict
    status_code: int = HTTPStatus.NOT_ACCEPTABLE


# 500
@dataclass
class ServerError(HTTPError):
    message: dict
    status_code: int = HTTPStatus.INTERNAL_SERVER_ERROR

"""Navigator Exceptions."""


class NavException(Exception):
    """Base class for other exceptions"""

    state: int = 0

    def __init__(self, message: str = '', state: int = 0, *args, **kwargs):
        super().__init__(message)
        self.message = message
        self.state = int(state)

    def __str__(self):
        return f"{self.message}"

    def get(self):
        return self.message


class UserDoesntExists(NavException):
    state: int = 404


class InvalidAuth(NavException):
    state: int = 401

class FailedAuth(NavException):
    state: int = 403

class AuthExpired(NavException):
    state: int = 403

class ValidationError(NavException):
    state: int = 406
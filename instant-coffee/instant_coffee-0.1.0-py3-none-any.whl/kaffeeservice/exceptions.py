"""
This module implements kaffeeservice errors
"""
class ServiceException(Exception):
    """
   Service exception base
   """

    def __init__(self, status_code: int, d: str):
        self.status_code = status_code
        self.body = d
        super().__init__('Service exception: {} - Body: {}'.format(status_code, d))


class ConflictException(ServiceException):
    """
    Service Not Found Exception
    """

    def __init__(self, data: str):
        super().__init__(409, data)


class NotFoundException(ServiceException):
    """
    Service Not Found Exception
    """

    def __init__(self, data: str):
        super().__init__(404, data)


class ValidationException(ServiceException):
    """
    Service Validation Exception
    """

    def __init__(self, data: str):
        super().__init__(422, data)

EXCEPTIONS = {
    404: NotFoundException,
    409: ConflictException,
    422: ValidationException
}

def service_exception(status_code, data: bytes) -> ServiceException:
    """
    Get custom exception depending on status code

    :param status_code: http error code
    :param data: the exception data content

    :return: custom ServiceException
    """
    exc = EXCEPTIONS.get(status_code)
    if exc:
        return exc(data.decode('utf-8'))
    return ServiceException(status_code, data.decode('utf-8'))

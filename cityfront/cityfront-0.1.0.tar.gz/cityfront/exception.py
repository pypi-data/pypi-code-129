from typing import TYPE_CHECKING
from loguru import logger
if TYPE_CHECKING:
    from .response import Response


class CityFrontException(Exception):
    ...


class AuthCredentialError(CityFrontException):
    """Auth Credential Error"""


class AuthExpiredError(CityFrontException):
    """Auth Expired Error"""


class RequestFailed(CityFrontException):
    """Simple API request failed with error status code"""

    def __init__(self, response: "Response"):
        self.response = response

    def __repr__(self) -> str:
        
        return (
            f"<RequestFailed: {self.response.raw_request.method} "
            f"{self.response.raw_request.url}, status_code: {self.response.status_code}>"
        )
    @property
    def message(self):
        return self.response.json()["message"]
    
    def __str__(self) -> str:
        logger.error(self.response.raw_request.headers)
        logger.error(self.response.json())
        return self.__repr__()


class WebhookTypeNotFound(CityFrontException):
    """Webhook event type not found"""

    def __init__(self, name: str):
        self.name = name

    def __repr__(self) -> str:
        return f"<WebhookTypeNotFound: {self.name}>"

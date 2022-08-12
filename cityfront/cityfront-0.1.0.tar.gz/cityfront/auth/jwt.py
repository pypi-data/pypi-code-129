from dataclasses import dataclass
from typing import TYPE_CHECKING, Generator

import httpx

from .base import BaseAuthStrategy

if TYPE_CHECKING:
    from cityfront import AppWrite


@dataclass(slots=True)
class JwtAuth(httpx.Auth):
    """Admin Access Key Authentication Hook"""

    jwt_token: str

    def __init__(self, jwt_token: str):
        self.jwt_token = jwt_token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["X-Appwrite-Jwt"] = f"{self.jwt_token}"
        yield request


@dataclass(slots=True)
class JwtAuthStrategy(BaseAuthStrategy):
    """Personal Access Token Authentication"""

    jwt_token: str

    def get_auth_flow(self, appwrite: "AppWrite") -> httpx.Auth:
        return JwtAuth(self.jwt_token)

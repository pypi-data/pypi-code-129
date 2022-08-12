from dataclasses import dataclass
from typing import TYPE_CHECKING, Generator

import httpx

from .base import BaseAuthStrategy

if TYPE_CHECKING:
    from cityfront import AppWrite


@dataclass(slots=True)
class KeyAuth(httpx.Auth):
    """Admin Access Key Authentication Hook"""

    key_token: str

    def __init__(self, key_token: str):
        self.key_token = key_token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.headers["x-appwrite-key"] = f"{self.key_token}"
        # print(request.headers)
        yield request


@dataclass(slots=True)
class KeyAuthStrategy(BaseAuthStrategy):
    """Personal Access Token Authentication"""

    token: str

    def get_auth_flow(self, appwrite: "AppWrite") -> httpx.Auth:
        return KeyAuth(self.token)

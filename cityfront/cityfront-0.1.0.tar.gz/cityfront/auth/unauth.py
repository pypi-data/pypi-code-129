from typing import TYPE_CHECKING

import httpx

from .base import BaseAuthStrategy

if TYPE_CHECKING:
    from cityfront import AppWrite


class UnauthAuthStrategy(BaseAuthStrategy):
    """Unauthenticated Cityfront"""

    def get_auth_flow(self, appwrite: "AppWrite") -> httpx.Auth:
        return httpx.Auth()

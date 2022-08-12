import abc
from typing import TYPE_CHECKING

import httpx

if TYPE_CHECKING:
    from cityfront import AppWrite


class BaseAuthStrategy(abc.ABC):
    @abc.abstractmethod
    def get_auth_flow(self, appwrite: "AppWrite") -> httpx.Auth:
        raise NotImplementedError

from httpx import AsyncClient
from pydantic import BaseModel
from pydantic.dataclasses import dataclass

# from appwrite.client import Client

# from appwrite.services.account import Account
from cityfront.constants import PROJECT_HEADER, APIKEY, JWT_SECRET, APPWRITE_LOCALE
from loguru import logger as log


def strip_urlpath(url: str):
    return url.strip().strip("/")


class ClientBase:
    def __init__(self, base_url: str = "https://api.appwrite.io/v1"):
        self._chunk_size = 5 * 1024 * 1024
        self._self_signed = False
        self._endpoint = base_url
        self._global_headers = {
            "content-type": "content-type",
            "x-sdk-version": "appwrite:python:0.10.0",
            "X-Appwrite-Response-Format": "0.15.0",
        }
        self._client = self.init_client()

    def init_client(self):
        _client = AsyncClient(
            base_url=self._endpoint,
            headers=self._global_headers,
            verify=(not self._self_signed),
        )
        return _client

    def add_header(self, key: str, value: str):
        self._global_headers[key.lower()] = value
        return self

    @property
    def jwt_key(self):
        """The jwt_key property."""
        return self._jwt_key

    @jwt_key.setter
    def jwt_key(self, value):
        self._jwt_key = value
        self.add_header(JWT_SECRET, value)

    @property
    def project(self):
        """The project property."""
        return self._project

    @project.setter
    def project(self, value):
        self._project = value
        self.add_header(PROJECT_HEADER, value)

    @property
    def api_key(self):
        """The api_key property."""
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value
        self.add_header(APIKEY, value)

    @property
    def locale(self):
        """The locale property."""
        return self._locale

    @locale.setter
    def locale(self, value):
        self._locale = value
        self.add_header(APPWRITE_LOCALE, value)

    def set_self_signed(self):
        self._self_signed = True
        self._client = self.init_client()
        return self

    @property
    def client(self) -> AsyncClient:
        """The client property."""
        return self._client

    def create_path(self, path: str):
        return f"{self._endpoint}/{path.strip().strip('/')}"

    def extract_data(self, data: dict | BaseModel | None):
        if data is None:
            return None
        if isinstance(data, BaseModel):
            return data.dict()
        elif isinstance(data, dict):
            return data
        elif isinstance(data, list):
            return [self.extract_data(item) for item in data]
        else:
            return data

    def merge_headers(self, headers: dict | None = None):
        soft_copy = {}
        soft_copy.update(self._global_headers)
        headers = headers or {}
        soft_copy.update(headers)
        return soft_copy

    def req_encode(self, data: dict, headers: dict):
        if headers["content-type"] == "application/json":
            return dict(json=data)
        else:

            return dict(data=data)

    async def get(
        self,
        path: str,
        headers: dict | None = None,
        params: BaseModel | dict | None = None,
    ):
        headers = self.merge_headers(headers)
        params = self.extract_data(params)

        return await self._client.get(
            self.create_path(path),
            headers=headers,
            params=params,
            verify=(not self._self_signed),
        )

    async def post(
        self,
        path: str,
        headers: dict | None = None,
        params: BaseModel | dict | None = None,
        data: BaseModel | dict | None = None,
    ):
        headers = self.merge_headers(headers)
        params = self.extract_data(params)
        data = self.extract_data(data)

        return await self._client.post(
            self.create_path(path),
            headers=headers,
            params=params,
            **self.req_encode(data, headers),
        )

    async def put(
        self,
        path: str,
        headers: dict | None = None,
        params: BaseModel | dict | None = None,
        data: BaseModel | dict | None = None,
    ):
        headers = self.merge_headers(headers)
        params = self.extract_data(params)
        data = self.extract_data(data)
        return await self._client.put(
            self.create_path(path),
            headers=headers,
            params=params,
            **self.req_encode(data, headers),
        )

    async def delete(
        self,
        path: str,
        headers: dict | None = None,
        params: BaseModel | dict | None = None,
    ):
        headers = self.merge_headers(headers)
        params = self.extract_data(params)
        return await self._client.delete(
            self.create_path(path),
            headers=headers,
            params=params,
        )

    async def upload(self, path: str, headers=None, params=None, data=None):
        headers = headers or {}
        headers.update(self._global_headers)
        return await self._client.post(
            self.create_path(path),
            headers=headers,
            params=params,
            **self.req_encode(data, headers),
        )

    async def patch(
        self,
        path: str,
        headers: dict | None = None,
        params: BaseModel | dict | None = None,
        data: BaseModel | dict | None = None,
    ):
        headers = self.merge_headers(headers)
        params = self.extract_data(params)
        data = self.extract_data(data)
        return await self._client.patch(
            self.create_path(path),
            headers=headers,
            params=params,
            **self.req_encode(data, headers),
        )

    # async def download(self, path, headers=None, params=None):
    #     headers = headers or {}
    #     headers.update(self._global_headers)
    #     return await self._client.get(self._endpoint +


class BaseService:
    def __init__(self, client: ClientBase, service_path: str = "/") -> None:
        self._client = client
        self.service_base = service_path

    @property
    def client(self) -> ClientBase:
        """The client property."""
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def service_base(self):
        """The service_url property."""
        return self._service_url

    @service_base.setter
    def service_base(self, value):
        self._service_url = value

    # @property
    # def service_url(self) -> str:
    #     """The service_path property."""
    #     return f"{}/"

    def svc_path(self, path: str) -> str:
        return f"{strip_urlpath(self.service_base)}/{path.strip().strip('/')}"

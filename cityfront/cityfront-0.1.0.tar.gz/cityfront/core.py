from types import TracebackType
from functools import cached_property
from typing_extensions import ParamSpec
from contextlib import contextmanager, asynccontextmanager
from typing import (
    Any,
    Dict,
    List,
    Type,
    Union,
    Generic,
    TypeVar,
    Callable,
    Optional,
    Awaitable,
    Generator,
    AsyncGenerator,
    cast,
    overload,
)

import httpx


from .response import Response

try:
    from .rest import RestNamespace
except (ImportError, SyntaxError):
    None

from .paginator import Paginator
from .exception import RequestFailed
from .config import Config, get_config
from .auth import (
    BaseAuthStrategy,
    TokenAuthStrategy,
    UnauthAuthStrategy,
    KeyAuthStrategy,
    JwtAuthStrategy,
)
from .typing import (
    URLTypes,
    CookieTypes,
    HeaderTypes,
    ContentTypes,
    RequestFiles,
    QueryParamTypes,
)

T = TypeVar("T")
A = TypeVar("A", bound="BaseAuthStrategy")
A_o = TypeVar("A_o", bound="BaseAuthStrategy")

CP = ParamSpec("CP")
CT = TypeVar("CT")
RT = TypeVar("RT")

R = Union[
    Callable[CP, Response[List[RT]]],
    Callable[CP, Awaitable[Response[List[RT]]]],
]


class AppWrite(Generic[A]):
    # none auth with config
    @overload
    def __init__(
        self: "AppWrite[UnauthAuthStrategy]",
        auth: None = None,
        *,
        config: Config,
    ):
        ...

    # token auth with config
    @overload
    def __init__(
        self: "AppWrite[TokenAuthStrategy]",
        auth: str,
        *,
        config: Config,
    ):
        ...

    # other auth strategies with config
    @overload
    def __init__(
        self: "AppWrite[A]",
        auth: A,
        *,
        config: Config,
    ):
        ...

    # none auth without config
    @overload
    def __init__(
        self: "AppWrite[UnauthAuthStrategy]",
        auth: None = None,
        *,
        base_url: Optional[Union[str, httpx.URL]] = None,
        accept_format: Optional[str] = None,
        previews: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
        project_id: Optional[str] = None,
    ):
        ...

    # token auth without config
    @overload
    def __init__(
        self: "AppWrite[TokenAuthStrategy]",
        auth: str,
        *,
        base_url: Optional[Union[str, httpx.URL]] = None,
        accept_format: Optional[str] = None,
        previews: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
        project_id: Optional[str] = None,
    ):
        ...

    # other auth strategies without config
    @overload
    def __init__(
        self: "AppWrite[A]",
        auth: A,
        *,
        base_url: Optional[Union[str, httpx.URL]] = None,
        accept_format: Optional[str] = None,
        previews: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
        project_id: Optional[str] = None,
    ):
        ...

    def __init__(
        self,
        auth: Optional[Union[A, str]] = None,
        *,
        config: Optional[Config] = None,
        base_url: Optional[Union[str, httpx.URL]] = None,
        accept_format: Optional[str] = None,
        previews: Optional[List[str]] = None,
        user_agent: Optional[str] = None,
        follow_redirects: bool = True,
        timeout: Optional[Union[float, httpx.Timeout]] = None,
        project_id: Optional[str] = None,
    ):
        auth = auth or UnauthAuthStrategy()
        self.auth: A = TokenAuthStrategy(auth) if isinstance(auth, str) else auth

        self.config = config or get_config(
            base_url,
            accept_format,
            previews,
            user_agent,
            follow_redirects,
            timeout,
            project_id,
        )

        self.__sync_client: Optional[httpx.Client] = None
        self.__async_client: Optional[httpx.AsyncClient] = None

    # sync context
    def __enter__(self):
        if self.__sync_client is not None:
            raise RuntimeError("Cannot enter sync context twice")
        self.__sync_client = self._create_sync_client()
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ):
        cast(httpx.Client, self.__sync_client).close()
        self.__sync_client = None

    # async context
    async def __aenter__(self):
        if self.__async_client is not None:
            raise RuntimeError("Cannot enter async context twice")
        self.__async_client = self._create_async_client()
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]] = None,
        exc_value: Optional[BaseException] = None,
        traceback: Optional[TracebackType] = None,
    ):
        await cast(httpx.AsyncClient, self.__async_client).aclose()
        self.__async_client = None

    # default args for creating client
    def _get_client_defaults(self):
        return {
            "auth": self.auth.get_auth_flow(self),
            "base_url": self.config.base_url,
            "headers": {
                # "User-Agent": self.config.user_agent,
                # "Accept": self.config.accept,
                "X-Appwrite-Project": self.config.project_id,
                "x-sdk-version": "appwrite:python:0.10.0",
                "X-Appwrite-Response-Format": "0.15.0",
            },
            "timeout": self.config.timeout,
            "follow_redirects": self.config.follow_redirects,
            "verify": False,
        }

    # create sync client
    def _create_sync_client(self) -> httpx.Client:
        return httpx.Client(**self._get_client_defaults())

    # get or create sync client
    @contextmanager
    def get_sync_client(self) -> Generator[httpx.Client, None, None]:
        if self.__sync_client:
            yield self.__sync_client
        else:
            client = self._create_sync_client()
            try:
                yield client
            finally:
                client.close()

    # create async client
    def _create_async_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(**self._get_client_defaults())

    # get or create async client
    @asynccontextmanager
    async def get_async_client(self) -> AsyncGenerator[httpx.AsyncClient, None]:
        if self.__async_client:
            yield self.__async_client
        else:
            client = self._create_async_client()
            try:
                yield client
            finally:
                await client.aclose()

    # sync request
    def _request(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> httpx.Response:
        with self.get_sync_client() as client:
            return client.request(
                method,
                url,
                params=params,
                content=content,
                data=data,
                files=files,
                json=json,
                headers=headers,
                cookies=cookies,
            )

    # async request
    async def _arequest(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
    ) -> httpx.Response:
        async with self.get_async_client() as client:
            return await client.request(
                method,
                url,
                params=params,
                content=content,
                data=data,
                files=files,
                json=json,
                headers=headers,
                cookies=cookies,
            )

    # check and parse response
    def _check(
        self,
        response: httpx.Response,
        response_model: Type[T] = Any,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[T]:
        if response.is_error:
            error_models = error_models or {}
            status_code = str(response.status_code)
            error_model = error_models.get(
                status_code,
                error_models.get(
                    f"{status_code[:-2]}XX", error_models.get("default", Any)
                ),
            )
            rep = Response(response, error_model)
            raise RequestFailed(rep)
        return Response(response, response_model)

    # sync request and check
    def request(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        # cookies: Optional[CookieTypes] =,
        cookies: Optional[CookieTypes] = None,
        response_model: Type[T] = Any,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[T]:
        # cookies = cookies or httpx.Cookies()
        # cookies.set("a_session_62ea325a84fe91d4179d", "eyJpZCI6IjYyZjVmNjBmYTZmNzI3NjM3NmFjIiwic2VjcmV0IjoiYTY0MWI3YzA1Njk0ZTJjYzg1YjMyYWIxOTVhNjQ4OTcxNWU4YjBmYjU2ZjgxMDEwNjAyMDViNTM0MGVlODllMzMzOTE0N2VjOWQ4ZjI5OWQxODY4ZjE3MDljM2FiM2NhZTg4MmQ1NGVkMWE2MDI5Nzk2ZjIwMTljZTJmYzU0MWEyMGFhODRiM2FhZjBhY2Q3OWQ4OGQ0MWQzYTI2NDNjMmE3ODE2ODU4ZGMzZTkzNzM0MDBlMDFmODFhZTBlZjc4MmRlYTI4MGYwYzUwYzAxMjMwOWNjMTM4ZDFiMmQxYjUyNzc1ODliMmU4YTZkZTA1YTEwZWE1MGNjMmQ0ZTZkMCJ9", domain="appwrite.autoworkz.org")
        # cookies.set("a_session_62ea325a84fe91d4179d_legacy", "eyJpZCI6IjYyZjVmNjBmYTZmNzI3NjM3NmFjIiwic2VjcmV0IjoiYTY0MWI3YzA1Njk0ZTJjYzg1YjMyYWIxOTVhNjQ4OTcxNWU4YjBmYjU2ZjgxMDEwNjAyMDViNTM0MGVlODllMzMzOTE0N2VjOWQ4ZjI5OWQxODY4ZjE3MDljM2FiM2NhZTg4MmQ1NGVkMWE2MDI5Nzk2ZjIwMTljZTJmYzU0MWEyMGFhODRiM2FhZjBhY2Q3OWQ4OGQ0MWQzYTI2NDNjMmE3ODE2ODU4ZGMzZTkzNzM0MDBlMDFmODFhZTBlZjc4MmRlYTI4MGYwYzUwYzAxMjMwOWNjMTM4ZDFiMmQxYjUyNzc1ODliMmU4YTZkZTA1YTEwZWE1MGNjMmQ0ZTZkMCJ9", domain="appwrite.autoworkz.org")
        raw_resp = self._request(
            method,
            url,
            params=params,
            content=content,
            data=data,
            files=files,
            json=json,
            headers=headers,
            cookies=cookies,
        )
        return self._check(raw_resp, response_model, error_models)

    # async request and check
    async def arequest(
        self,
        method: str,
        url: URLTypes,
        *,
        params: Optional[QueryParamTypes] = None,
        content: Optional[ContentTypes] = None,
        data: Optional[dict] = None,
        files: Optional[RequestFiles] = None,
        json: Optional[Any] = None,
        headers: Optional[HeaderTypes] = None,
        cookies: Optional[CookieTypes] = None,
        response_model: Type[T] = Any,
        error_models: Optional[Dict[str, type]] = None,
    ) -> Response[T]:
        raw_resp = await self._arequest(
            method,
            url,
            params=params,
            content=content,
            data=data,
            files=files,
            json=json,
            headers=headers,
            cookies=cookies,
        )
        return self._check(raw_resp, response_model, error_models)

    # copy github instance with other auth
    #  ! Should use this with_auth method to change the jwt and key headers.
    def with_auth(self, auth: A_o) -> "AppWrite[A_o]":
        return AppWrite(auth=auth, config=self.config.copy())

    # high level methods

    def project_id(self) -> str:
        return self.config.project_id

    def project_key(self) -> str:
        return self.config.project_key

    def use_jwt(self, jwt_token: str) -> "AppWrite[A_o]":
        """
        Switch to using a JWT token for authentication.
        Replaces the current jwt and server keys.
        """
        return self.with_auth(JwtAuthStrategy(jwt_token))

    def use_key(self, admin_key: str) -> "AppWrite[A_o]":
        """
        Switch to using an admin key for authentication.
        Replaces the current jwt and server keys.
        """
        return self.with_auth(KeyAuthStrategy(admin_key))

    # rest api
    @cached_property
    def rest(self) -> RestNamespace:
        return RestNamespace(self)

    @cached_property
    def aclient(self):
        if self.__async_client is not None:
            return self.__async_client
        self.__async_client = self._create_async_client()
        return self.__async_client

    @cached_property
    def client(self):
        if self.__sync_client is not None:
            return self.__sync_client
        self.__sync_client = self._create_sync_client()
        return self.__sync_client

    # rest pagination
    @overload
    @staticmethod
    def paginate(
        request: R,
        page: int = 1,
        per_page: int = 100,
        map_func: None = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        ...

    @overload
    @staticmethod
    def paginate(
        request: R,
        page: int = 1,
        per_page: int = 100,
        map_func: Callable[[Response[List[CT]]], List[RT]] = ...,  # type: ignore
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        ...

    @staticmethod
    def paginate(
        request: R,
        page: int = 1,
        per_page: int = 100,
        map_func: Optional[Callable[[Response[List[CT]]], List[RT]]] = None,
        *args: CP.args,
        **kwargs: CP.kwargs,
    ) -> Paginator[RT]:
        return Paginator(request, page, per_page, map_func, *args, **kwargs)  # type: ignore

    def __str__(self) -> str:
        return "AppWrite(base_url='{}', project_id='{}')".format(self.config.base_url, self.config.project_id)
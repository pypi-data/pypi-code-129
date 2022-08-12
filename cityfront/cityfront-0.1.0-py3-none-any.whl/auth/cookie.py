"""Create a Cookie Auth that can act as the base for both the JWT and Token Auth strategies"""


from dataclasses import dataclass
from typing import TYPE_CHECKING, Generator
from diskcache import Cache
import httpx
from loguru import logger as log
from .base import BaseAuthStrategy

if TYPE_CHECKING:
    from cityfront import AppWrite

cookie_cache = Cache("/tmp")
COOKIE_KEY = "cookie-store"




@dataclass(slots=True)
class CookieAuth(httpx.Auth):
    """Admin Access Key Authentication Hook"""


    # def __init__(self):
    #     self.jwt_token = jwt_token

    def auth_flow(
        self, request: httpx.Request
    ) -> Generator[httpx.Request, httpx.Response, None]:
        request.cookies = self.check_local_cookies()
            
        # request.headers["X-Appwrite-Jwt"] = f"{self.jwt_token}"
        response = yield request
        self.update_cookies_if_exists(response)
    
    
    def check_local_cookies(self) -> httpx.Cookies | None:
        """Check if the there's saved cookie code. """
        request_cookies = httpx.Cookies()
        log.warning(COOKIE_KEY in cookie_cache)
        if COOKIE_KEY in cookie_cache:
            
            
            stored = cookie_cache[COOKIE_KEY]
            match stored:
                case httpx.Cookies() as prior_cookie:
                    request_cookies = httpx.Cookies(prior_cookie)
                case dict() as cookie:
                    request_cookies = request_cookies.update(cookie)
                case _:
                    log.info("No cookies to update")
                    
        return request_cookies
    
    def update_cookies_if_exists(self, response: httpx.Response):
        """Update the local cookie store if it exists"""
        local_cookies = httpx.Cookies()
        # log.critical((len(local_cookies) > 0))
        
        local_cookies.extract_cookies(response)
        log.critical((len(local_cookies) > 0))
        log.critical((dict(local_cookies.items())))
        if len(local_cookies) > 0:
            cookie_cache[COOKIE_KEY] = dict(local_cookies.items())
        # cookie_cache[COOKIE_KEY] = 
        # if len(response.cookies) > 0:
        #     cookie_cache[COOKIE_KEY] = response.cookies.extract_cookies()
        # if COOKIE_KEY in response.cookies:
        #     cookie_cache[COOKIE_KEY] = response.cookies
            
        

@dataclass(slots=True)
class CookieAuthStrategy(BaseAuthStrategy):
    """Personal Access Token Authentication"""

    # jwt_token: str

    def get_auth_flow(self, appwrite: "AppWrite") -> httpx.Auth:
        return CookieAuth()

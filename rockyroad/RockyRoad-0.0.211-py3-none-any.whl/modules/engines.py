from .module_imports import *


@headers({"Ocp-Apim-Subscription-Key": key})
class Engines(Consumer):
    """Inteface to Inspection resource for the RockyRoad API."""

    def __init__(self, Resource, *args, **kw):
        self._base_url = Resource._base_url
        super().__init__(base_url=Resource._base_url, *args, **kw)

    def catalog(self):
        return self.__Catalog(self)

    @headers({"Ocp-Apim-Subscription-Key": key})
    class __Catalog(Consumer):
        """Inteface to Warranty Credit Request resource for the RockyRoad API."""

        def __init__(self, Resource, *args, **kw):
            super().__init__(base_url=Resource._base_url, *args, **kw)
        
        @returns.json
        @http_get("engines/catalog/vendors")
        def vendors(
            self,
        ):
            """This call will return specified info for the specified criteria."""

        @returns.json
        @http_get("engines/catalog/{uid}")
        def get(
            self,
            uid: str
        ):
            """This call will return specified info for the specified criteria."""

        @returns.json
        @http_get("engines/catalog")
        def list(
            self,
            vendor: Query(type=str) = None,
        ):
            """This call will return specified info for the specified criteria."""

        @returns.json
        @json
        @post("engines/catalog")
        def insert(self, engine_catalog: Body):
            """This call will create specified info with the specified parameters."""

        @returns.json
        @delete("engines/catalog/{uid}")
        def delete(self, uid: str):
            """This call will delete specified info for the specified uid."""

        @returns.json
        @json
        @patch("engines/catalog")
        def update(self, engine_catalog: Body):
            """This call will update specified info with the specified parameters."""

        


    @returns.json
    @json
    @post("engines")
    def insert(self, engine_and_machine: Body):
        """This call will create specified info with the specified parameters."""

    @returns.json
    @http_get("engines")
    def list(
        self,
    ):
        """This call will return specified info for the specified criteria."""

    @returns.json
    @http_get("engines/{uid}")
    def get(self, uid: str):
        """This call will return specified info for the specified criteria."""

    @returns.json
    @delete("engines/{uid}")
    def delete(self, uid: str):
        """This call will delete specified info for the specified uid."""

    @returns.json
    @json
    @patch("engines")
    def update(self, engine_and_machine: Body):
        """This call will update specified info with the specified parameters."""


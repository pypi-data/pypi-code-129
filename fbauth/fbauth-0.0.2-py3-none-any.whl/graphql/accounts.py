# -*- coding: utf-8 -*-
"""
    API - CRUD
"""

import functools

# Fastberry
import strawberry
from fastberry import GQL
from fastberry.graphql.inputs import Pagination
from fastberry.graphql.types import (
    Edges,
    Error,
    ErrorMessage,
    Mutation,
    Query,
    Response,
)

from .. import actions, types
from ..database import SQL

sql_manager = SQL(types.User)


# Create your API (GraphQL) here.
class Accounts(GQL):
    """Demo Api"""

    schema = None
    prefix = "account"

    class Query:
        """Query"""

        async def search(info) -> str:
            """Read the Docs"""
            print(info)
            return "Search"

        async def detail(info, id: str) -> str:
            """Read the Docs"""
            return "detail"

    class Mutation:
        """Mutation"""

        async def create(username: str, password: str, email: str) -> str:
            return "create"

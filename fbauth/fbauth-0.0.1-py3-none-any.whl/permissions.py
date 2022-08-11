# -*- coding: utf-8 -*-
""" [Permission]
    Check GraphQL Context for a { User } or { Anonymous-User }.
"""

import typing

from fastberry import BasePermission
from strawberry.types import Info

from .actions import User


class IsAuthorized(BasePermission):
    """Check If User Is Authorized"""

    message = "User is not authorized"  # Unauthorized

    async def has_permission(self, source: typing.Any, info: Info, **kwargs) -> bool:
        """Check GraphQL's Info Context"""

        operation = info.field_name  # info.python_name
        user = info.context.get("user")
        if user:
            if user.is_super_user:
                return True
            else:
                permissions = await User.get_perms(user.role_id)
                return operation in permissions
        return False

"""
Decorators that warn about code maturity.
"""
from __future__ import annotations

import enum as _enum
from functools import wraps as _wraps
from typing import Optional as _Optional
from typing import Union as _Union
from warnings import warn as _warn


class CodeIncompleteError(NotImplementedError):
    """The code is not finished."""


class CodeRemovedError(NotImplementedError):
    """The code was removed."""


class PreviewWarning(UserWarning):
    """The code being called is a preview, unstable. or immature."""


@_enum.unique
class CodeStatus(_enum.Enum):
    """
    An enum for the quality/maturity of code,
    ranging from incomplete to deprecated.
    """

    INCOMPLETE = -2
    PREVIEW = -1
    STABLE = 0
    PENDING_DEPRECATION = 1
    DEPRECATED = 2
    REMOVED = 3

    @classmethod
    def of(cls, x: _Union[int, str, CodeStatus]) -> CodeStatus:
        if isinstance(x, str):
            return cls[x.lower().strip()]
        if isinstance(x, CodeStatus):
            return x
        if isinstance(x, int):
            return cls(x)
        raise TypeError(f"Invalid type {type(x)} for {x}")


def status(
    level: _Union[int, str, CodeStatus], vr: _Optional[str] = "", msg: _Optional[str] = None
):
    """
    Annotate code quality. Emits a warning if bad code is called.

    Args:
        level: The quality / maturity
        vr: First version the status / warning applies to
        msg: Explanation and/or when it will be removed or completed
    """

    level = CodeStatus.of(level)

    @_wraps(status)
    def dec(func):
        func.__status__ = level
        if level is CodeStatus.STABLE:
            return func
        elif level is CodeStatus.REMOVED:

            def my_fn(*args, **kwargs):
                raise CodeRemovedError(f"{func.__name__} was removed (as of version: {vr}). {msg}")

            return _wraps(func)(my_fn)

        elif level is CodeStatus.INCOMPLETE:

            def my_fn(*args, **kwargs):
                raise CodeIncompleteError(
                    f"{func.__name__} is incomplete (as of version: {vr}). {msg}"
                )

            return _wraps(func)(my_fn)
        elif level is CodeStatus.PREVIEW:

            def my_fn(*args, **kwargs):
                _warn(
                    f"{func.__name__} is a preview or immature (as of version: {vr}). {msg}",
                    PreviewWarning,
                )
                return func(*args, **kwargs)

            return _wraps(func)(my_fn)
        elif level is CodeStatus.PENDING_DEPRECATION:

            def my_fn(*args, **kwargs):
                _warn(
                    f"{func.__name__} is pending deprecation (as of version: {vr}). {msg}",
                    PendingDeprecationWarning,
                )
                return func(*args, **kwargs)

            return _wraps(func)(my_fn)
        elif level is CodeStatus.DEPRECATED:

            def my_fn(*args, **kwargs):
                _warn(
                    f"{func.__name__} is deprecated (as of version: {vr}). {msg}",
                    DeprecationWarning,
                )
                return func(*args, **kwargs)

            return _wraps(func)(my_fn)
        raise AssertionError(f"What is {level}?")

    return dec

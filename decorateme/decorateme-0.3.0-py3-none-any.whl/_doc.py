"""
Decorators for manipulating docstrings.
"""

from functools import wraps as _wraps
from typing import Type


def copy_docstring(from_obj: Type) -> None:
    """
    Copies the docstring from `from_obj` to this function or class.
    """

    @_wraps(copy_docstring)
    def dec(myobj):
        myobj.__doc__ = from_obj.__doc__
        return myobj

    return dec


def append_docstring(from_obj: Type) -> None:
    """
    Appends the docstring from `from_obj` to the docstring for this function or class.
    """

    @_wraps(append_docstring)
    def dec(myobj):
        myobj.__doc__ += from_obj.__doc__
        return myobj

    return dec

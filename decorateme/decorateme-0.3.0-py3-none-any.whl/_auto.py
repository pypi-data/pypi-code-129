"""
Decorators for adding dunder methods automatically.
"""
from functools import wraps as _wraps
from typing import AbstractSet, Callable, Optional

from decorateme._utils import _InfoSpecialStr, _SpecialStr, _Utils


def auto_utils():
    """
    Auto-adds __repr__, __str__, etc., for simple utility classes with no attributes.
    """

    def __str(self):
        return self.__class__.__name__

    def __repr(self):
        return self.__class__.__name__

    def __hash(self):
        return _Utils.auto_hash(self, only=None, exclude=None)

    def __eq(self, o):
        return _Utils.auto_eq(self, o, only=None, exclude=None)

    @_wraps(auto_obj)
    def dec(cls):
        cls.__eq__ = __eq
        cls.__str__ = __str
        cls.__repr__ = __repr
        cls.__hash__ = __hash
        return cls

    return dec


def auto_obj():
    """
    Auto-adds ``__eq__``, ``__hash__``, ``__repr__``, ``__str__``, and ``_repr_html``.
    See the decorators for auto_eq, auto_hash, and auto_repr for more details.
    """

    def __str(self):
        return _Utils.gen_str(self, exclude=lambda a: a.startswith("_"), with_address=False)

    def __html(self):
        return _SpecialStr(
            _Utils.gen_str(
                self,
                only=None,
                exclude=lambda a: a.startswith("_"),
                with_address=True,
                bold_surround=lambda c: "<strong>" + c + "</strong>",
            )
        )

    def __repr(self):
        return _Utils.gen_str(self, exclude=lambda _: False, with_address=True)

    def __hash(self):
        return _Utils.auto_hash(self, only=None, exclude=None)

    def __eq(self, o):
        return _Utils.auto_eq(self, o, only=None, exclude=None)

    @_wraps(auto_obj)
    def dec(cls):
        cls.__eq__ = __eq
        cls.__str__ = __str
        cls.__repr__ = __repr
        cls.__hash__ = __hash
        cls._repr_html_ = __html
        return cls

    return dec


def auto_eq(
    only: Optional[AbstractSet[str]] = None, exclude: Optional[Callable[[str], bool]] = None
):
    """
    Auto-adds a __eq__ function by comparing its attributes.

    Args:
        only: Only include these attributes
        exclude: Exclude these attributes
    """

    @_wraps(auto_eq)
    def dec(cls):
        def __eq(self, other):
            return _Utils.auto_eq(self, other, only, exclude)

        cls.__eq__ = __eq
        return cls

    return dec


def auto_hash(
    only: Optional[AbstractSet[str]] = None, exclude: Optional[Callable[[str], bool]] = None
):
    """
    Auto-adds a __hash__ function by hashing its attributes.

    Args:
        only: Only include these attributes
        exclude: Exclude these attributes
    """

    @_wraps(auto_hash)
    def dec(cls):
        def __hash(self):
            return _Utils.auto_hash(self, only, exclude)

        cls.__hash__ = __hash
        return cls

    return dec


def auto_repr(
    only: Optional[AbstractSet[str]] = None,
    exclude: Optional[Callable[[str], bool]] = lambda a: False,
):
    """
    Auto-adds __repr__ and __str__.

    Args:
        only: Only include these attributes
        exclude: Exclude these attributes
    """

    @_wraps(auto_repr)
    def dec(cls):
        def __repr(self):
            return _Utils.gen_str(self, only=only, exclude=exclude, with_address=True)

        cls.__repr__ = __repr
        return cls

    return dec


def auto_str(
    only: Optional[AbstractSet[str]] = None,
    exclude: Optional[Callable[[str], bool]] = lambda a: a.startswith("_"),
    with_address: bool = False,
):
    """
    Auto-adds ``__str__``.

    Args:
        only: Only include these attributes
        exclude: Exclude these attributes
        with_address: Include the hex memory address
    """

    @_wraps(auto_str)
    def dec(cls):
        def __str(self):
            return _Utils.gen_str(self, only=only, exclude=exclude, with_address=with_address)

        cls.__str__ = __str
        return cls

    return dec


def auto_html(
    only: Optional[AbstractSet[str]] = None,
    exclude: Optional[Callable[[str], bool]] = lambda a: lambda b: b.startswith("_"),
    with_address: bool = True,
):
    """
    Auto-adds a ``_repr_html`` method, which Jupyter will use.

    Args:
        only: Only include these attributes
        exclude: Exclude these attributes
        with_address: Include the hex memory address
    """

    @_wraps(auto_html)
    def dec(cls):
        def __html(self):
            return _SpecialStr(
                _Utils.gen_str(
                    self,
                    only=only,
                    exclude=exclude,
                    with_address=with_address,
                    bold_surround=lambda c: "<strong>" + c + "</strong>",
                    em_surround=lambda c: "<em>" + c + "</em>",
                )
            )

        cls._repr_html = __html
        return cls

    return dec


def auto_repr_str(
    exclude_simple: Optional[Callable[[str], bool]] = lambda a: a.startswith("_"),
    exclude_html: Optional[Callable[[str], bool]] = lambda a: a.startswith("_"),
    exclude_all: Optional[Callable[[str], bool]] = lambda a: False,
):
    """
    Decorator.
    Auto-adds ``__repr__``, ``__str__``, and ``_repr_html_`` that show the attributes:
        - ``__str__`` will include attributes in neither ``exclude_all`` nor ``exclude_simple``
        - ``_repr_html_`` will include attributes in neither ``exclude_all`` nor ``exclude_simple``
            and will show the hexadecimal address
        - ``__repr__`` will include attributes not in exclude_all and will show the hexadecimal address

    The ``_repr_html_`` will be used by Jupyter display.

    Example:

        .. code-block::

            repr(point) == Point(angle=0.3, radius=4, _style='point' @ 0x5528ca3)
            str(point) == Point(angle=0.3, radius=4)
            _repr_html_(point) == Point(angle=0.3, radius=4 @ 0x5528ca3)

    Args:
        exclude_simple: Exclude attributes matching these names in human-readable strings (str and _repr_html)
        exclude_html: Exclude for _repr_html
        exclude_all: Exclude these attributes in all the functions
    """

    @_wraps(auto_repr_str)
    def dec(cls):
        def __str(self):
            return _Utils.gen_str(self, only=None, exclude=exclude_simple, with_address=False)

        def __html(self):
            return _SpecialStr(
                _Utils.gen_str(
                    self,
                    only=None,
                    exclude=exclude_html,
                    with_address=True,
                    bold_surround=lambda c: "<strong>" + c + "</strong>",
                    em_surround=lambda c: "<em>" + c + "</em>",
                )
            )

        def __repr(self):
            return _Utils.gen_str(self, only=None, exclude=exclude_all, with_address=True)

        cls.__str__ = __str
        cls.__repr__ = __repr
        cls._repr_html_ = __html
        return cls

    return dec


def auto_info(
    only: Optional[AbstractSet[str]] = None,
    exclude: Optional[Callable[[str], bool]] = lambda a: a.startswith("_"),
):
    """
    Auto-adds a function ``info`` that outputs a pretty multi-line representation of the instance and its attributes.

    Args:
        only: Only include these attributes
        exclude: Exclude these attributes
    """

    @_wraps(auto_info)
    def dec(cls):
        def __info(self):
            return _InfoSpecialStr(
                _Utils.gen_str(
                    self,
                    delim="\n\t",
                    eq=" = ",
                    opening="(\n\t",
                    closing="\n)",
                    with_address=False,
                    only=only,
                    exclude=exclude,
                )
            )

        cls.info = __info
        return cls

    return dec

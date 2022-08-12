"""
Decorators for types that are "basically" a simpler type.
"""
from functools import wraps as _wraps


def float_type(attribute: str):
    """
    Auto-adds a ``__float__`` using the ``__float__`` of some attribute.
    Used to annotate a class as being "essentially an float".

    Args:
        attribute: The name of the attribute of this class
    """

    def __f(self):
        return float(getattr(self, attribute))

    @_wraps(float_type)
    def dec(cls):
        cls.__float__ = __f
        return cls

    return dec


def int_type(attribute: str):
    """
    Auto-adds an ``__int__`` using the ``__int__`` of some attribute.
    Used to annotate a class as being "essentially an integer".

    Args:
        attribute: The name of the attribute of this class
    """

    def __f(self):
        return float(getattr(self, attribute))

    def __i(self):
        return float(getattr(self, attribute))

    @_wraps(int_type)
    def dec(cls):
        cls.__float__ = __f
        cls.__int__ = __i
        return cls

    return dec


def iterable_over(attribute: str):
    """
    Auto-adds an ``__iter__`` over elements in an iterable attribute.
    Used to annotate a class as being "essentially an iterable" over some elements.

    Args:
        attribute: The name of the attribute of this class
    """

    def __x(self):
        return iter(getattr(self, attribute))

    @_wraps(iterable_over)
    def dec(cls):
        cls.__iter__ = __x
        return cls

    return dec


def collection_over(attribute: str):
    """
    Auto-adds an ``__iter__`` and ``__len__`` over elements in a collection attribute.
    Used to annotate a class as being "essentially a collection" over some elements.

    Args:
        attribute: The name of the attribute of this class
    """

    def __len(self):
        return len(list(iter(getattr(self, attribute))))

    def __iter(self):
        return iter(getattr(self, attribute))

    @_wraps(collection_over)
    def dec(cls):
        cls.__iter__ = __iter
        cls.__len__ = __len
        return cls

    return dec


def sequence_over(attribute: str):
    """
    Auto-adds ``__getitem__`` and ``__len__`` over elements in an iterable attribute.
    Used to annotate a class as being "essentially a list" over some elements.

    Args:
        attribute: The name of the attribute of this class
    """

    def __len(self):
        return len(list(iter(getattr(self, attribute))))

    def __iter(self):
        return iter(getattr(self, attribute))

    def __item(self, e):
        if hasattr(getattr(self, attribute), "__getitem__"):
            return getattr(self, attribute)[e]
        return iter(getattr(self, attribute))

    @_wraps(sequence_over)
    def dec(cls):
        cls.__getitem__ = __item
        cls.__iter__ = __iter
        cls.__len__ = __len
        return cls

    return dec

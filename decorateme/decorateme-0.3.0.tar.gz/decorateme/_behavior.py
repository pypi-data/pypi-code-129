"""
Decorators that affect object or class behavior.
"""
import os
import signal
import time
from functools import wraps as _wraps
from warnings import warn as _warn


def takes_seconds_named(x, *args, **kwargs):
    """
    Prints a statement like "Call to calc_distances took 15.2s." after the function returns.
    """
    t0 = time.monotonic()
    results = x(*args, **kwargs)
    delta = round(time.monotonic() - t0, 1)
    print(f"Call to {x.__name} took {delta} s.")
    return results


def takes_seconds(x, *args, **kwargs):
    """
    Prints a statement like "Done. Took 15.2s." after the function returns.
    """
    t0 = time.monotonic()
    results = x(*args, **kwargs)
    print("Done. Took {}s.".format(round(time.monotonic() - t0, 1)))
    return results


def mutable(cls):
    """
    Just marks an object as mutable.
    """
    return cls


def immutable(mutableclass):
    """
    Decorator for making a slot-based class immutable.
    Taken almost verbatim from https://code.activestate.com/recipes/578233-immutable-class-decorator/
    Written by Oren Tirosh and released under the MIT license.
    """
    if not isinstance(type(mutableclass), type):
        raise TypeError("@immutable: must be applied to a new-style class")
    if not hasattr(mutableclass, "__slots__"):
        raise TypeError("@immutable: class must have __slots__")

    # noinspection PyPep8Naming
    class immutableclass(mutableclass):
        __slots__ = ()  # No __dict__, please

        def __new__(cls, *args, **kw):
            new = mutableclass(*args, **kw)  # __init__ gets called while still mutable
            new.__class__ = immutableclass  # locked for writing now
            return new

        def __init__(self, *args, **kw):  # Prevent re-init after __new__
            pass

    # Copy class identity:
    immutableclass.__name__ = mutableclass.__name__
    immutableclass.__module__ = mutableclass.__module__
    # Make read-only:
    for name, member in mutableclass.__dict__.items():
        if hasattr(member, "__set__"):
            setattr(immutableclass, name, property(member.__get__))
    return immutableclass


def auto_singleton(cls):
    """
    Makes it so the constructor returns a singleton instance.
    The constructor CANNOT take arguments.

    Example:
        .. code-block::

            @auto_singleton
            class MyClass: pass
            mysingleton = MyClass()
    """
    instances = {}

    def get_instance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return get_instance

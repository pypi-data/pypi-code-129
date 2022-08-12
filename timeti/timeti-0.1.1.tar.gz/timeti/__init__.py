"""
Serialize elapsed time of functions, loops and code blocks.

Copyright 2022 Ilia Lazarev
"""

__all__ = ["Stopwatch", "Clockface", "timing", "totime", "timer"]

from contextlib import contextmanager
from functools import wraps
from typing import Callable

from timeti.clockface import Clockface
from timeti.stopwatch import Stopwatch


@contextmanager
def timing(name: str = None, serialize: Callable = None):
    """Serialize elapsed time of code block."""
    mention = f" '{name}' "
    sw = Stopwatch()
    yield sw
    sw.pause()
    if serialize is not None:
        serialize(sw, name)
    else:
        print(f"Elapsed time of{mention}block: {sw.clockface}")


def totime(items, name: str = None, serialize: Callable = None):
    """Serialize elapsed time of iteration."""
    mention = f" '{name}' "
    sw = Stopwatch()
    for i, item in enumerate(items):
        yield sw, item
        sw.lap()
        with sw.paused():
            if serialize is not None:
                serialize(sw, name, i)
            else:
                lap = sw.laps[-1]
                print(f"Elapsed time of{mention}loop iteration {i}: {lap}")

    sw.pause()
    if serialize is not None:
        serialize(sw, name, i)
    else:
        print(f"Elapsed time of{mention}loop: {sw.clockface}")


def timer(serialize: Callable = None):
    """Serialize elapsed time of funciton (decorator)."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with timing(func.__name__):
                return func(*args, **kwargs)

        return wrapper

    return decorator

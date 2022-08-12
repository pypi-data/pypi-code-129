"""
serializer elapsed time of functions, loops and code blocks.

Copyright 2022 Ilia Lazarev
"""

__all__ = ["Stopwatch", "Clockface", "timing", "totime", "timer"]

from contextlib import contextmanager
from functools import wraps
from typing import Callable

from timeti.clockface import Clockface
from timeti.stopwatch import Stopwatch


def _mention(name):
    return "" if name is None else f" '{name}'"


def _func_serializer(sw, name):
    mention = _mention(name)
    print(f"Elapsed time of{mention} function: {sw.clockface}")


def _ctxm_serializer(sw, name):
    mention = _mention(name)
    print(f"Elapsed time of{mention} block: {sw.clockface}")


def _loop_serializer(sw, name, i):
    mention = _mention(name)
    if i is not None:
        lap = sw.laps[-1]
        print(f"Elapsed time of{mention} loop iteration {i}: {lap}")
    else:
        print(f"Elapsed time of{mention} loop: {sw.clockface}")


@contextmanager
def timing(name: str = None, serializer: Callable = None):
    """Serialize elapsed time of code block."""
    serializer = serializer or _ctxm_serializer
    sw = Stopwatch()
    yield sw
    sw.pause()
    serializer(sw, name)


def totime(items, name: str = None, serializer: Callable = None):
    """Serialize elapsed time of iteration."""
    serializer = serializer or _loop_serializer
    sw = Stopwatch()
    for i, item in enumerate(items):
        yield sw, item
        sw.lap()
        with sw.paused():
            serializer(sw, name, i)

    sw.pause()
    serializer(sw, name, None)


def timer(serializer: Callable = None):
    """Serialize elapsed time of funciton (decorator)."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with timing(func.__name__, serializer=_func_serializer):
                return func(*args, **kwargs)

        return wrapper

    return decorator

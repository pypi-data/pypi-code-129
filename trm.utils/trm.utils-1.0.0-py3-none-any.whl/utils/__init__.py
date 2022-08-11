"""package of generally useful classes and functions.

This package collects classes and functions that I regularly use but
have no clear home, and which are not enough on their own to justify
making separate packages for. Amongst other things, they include a
class for handling 3D vectors, and for dealing with command-line
arguments in a way that gives scripts a "memory" (cline).

"""

# import all objects from core into top-level namespace
from .core import *

__all__ = core.__all__

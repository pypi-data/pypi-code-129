__version__ = "0.1.0"
from .core import AppWrite
try:
    from .core import AppWrite
except ImportError:
    None

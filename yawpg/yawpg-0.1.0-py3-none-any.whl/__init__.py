"""
yawpg it's simple pages generator.
```
from yawpg import pagetor, yawpg
pagetor.add_page("super_page_name", "# Hello from superpage.")
yawpg.run(port=8080)
```
"""

from . import _defaults
from ._host import Yawpg as _Yawpg
from ._pagetor import Page
from ._pagetor import Pagetor as _Pagetor

__version__ = "0.1.0"

__all__ = [
    "pagetor",
    "yawpg",
    "Page",
]

pagetor = _Pagetor()
yawpg = _Yawpg()

"""
Metadata for decorateme.
"""

import logging
from importlib.metadata import PackageNotFoundError
from importlib.metadata import metadata as __load
from pathlib import Path

pkg = Path(__file__).absolute().parent.name
logger = logging.getLogger(pkg)
metadata = None
try:
    metadata = __load(pkg)
    __status__ = "Development"
    __copyright__ = "Copyright 2017–2022"
    __date__ = "2020-08-24"
    __uri__ = metadata["home-page"]
    __title__ = metadata["name"]
    __summary__ = metadata["summary"]
    __license__ = metadata["license"]
    __version__ = metadata["version"]
    __author__ = metadata["author"]
    __maintainer__ = metadata["maintainer"]
    __contact__ = metadata["maintainer"]
except PackageNotFoundError:  # pragma: no cover
    logger.error(f"Could not load package metadata for {pkg}. Is it installed?")

from abc import ABC, ABCMeta, abstractmethod
from dataclasses import dataclass
from functools import total_ordering
from typing import final

from decorateme._auto import (
    auto_eq,
    auto_hash,
    auto_html,
    auto_info,
    auto_obj,
    auto_repr,
    auto_repr_str,
    auto_str,
    auto_utils,
)
from decorateme._behavior import (
    auto_singleton,
    immutable,
    mutable,
    takes_seconds,
    takes_seconds_named,
)
from decorateme._doc import append_docstring, copy_docstring
from decorateme._informative import (
    external,
    internal,
    not_thread_safe,
    override_recommended,
    overrides,
    reserved,
    thread_safe,
)
from decorateme._over import (
    collection_over,
    float_type,
    int_type,
    iterable_over,
    sequence_over,
)
from decorateme._status import (
    CodeIncompleteError,
    CodeRemovedError,
    CodeStatus,
    PreviewWarning,
    status,
)

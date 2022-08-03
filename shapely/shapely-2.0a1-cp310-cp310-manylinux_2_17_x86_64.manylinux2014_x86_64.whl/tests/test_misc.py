import os
import sys
from itertools import chain
from string import ascii_letters, digits
from unittest import mock

import numpy as np
import pytest

import shapely
from shapely.decorators import multithreading_enabled, requires_geos


@pytest.fixture
def mocked_geos_version():
    with mock.patch.object(shapely.lib, "geos_version", new=(3, 7, 1)):
        yield "3.7.1"


@pytest.fixture
def sphinx_doc_build():
    os.environ["SPHINX_DOC_BUILD"] = "1"
    yield
    del os.environ["SPHINX_DOC_BUILD"]


def test_version():
    assert isinstance(shapely.__version__, str)


def test_geos_version():
    expected = "{0:d}.{1:d}.{2:d}".format(*shapely.geos_version)
    actual = shapely.geos_version_string

    # strip any beta / dev qualifiers
    if any(c.isalpha() for c in actual):
        if actual[-1].isnumeric():
            actual = actual.rstrip(digits)
        actual = actual.rstrip(ascii_letters)

    assert actual == expected


@pytest.mark.skipif(
    sys.platform.startswith("win") and shapely.geos_version[:2] == (3, 7),
    reason="GEOS_C_API_VERSION broken for GEOS 3.7.x on Windows",
)
def test_geos_capi_version():
    expected = "{0:d}.{1:d}.{2:d}-CAPI-{3:d}.{4:d}.{5:d}".format(
        *(shapely.geos_version + shapely.geos_capi_version)
    )

    # split into component parts and strip any beta / dev qualifiers
    (
        actual_geos_version,
        actual_geos_api_version,
    ) = shapely.geos_capi_version_string.split("-CAPI-")

    if any(c.isalpha() for c in actual_geos_version):
        if actual_geos_version[-1].isnumeric():
            actual_geos_version = actual_geos_version.rstrip(digits)
        actual_geos_version = actual_geos_version.rstrip(ascii_letters)
    actual_geos_version = actual_geos_version.rstrip(ascii_letters)

    assert (
        "{0}-CAPI-{1}".format(actual_geos_version, actual_geos_api_version) == expected
    )


def func():
    """Docstring that will be mocked.
    A multiline.

    Some description.
    """


class SomeClass:
    def func(self):
        """Docstring that will be mocked.
        A multiline.

        Some description.
        """


expected_docstring = """Docstring that will be mocked.
{indent}A multiline.

{indent}.. note:: 'func' requires at least GEOS {version}.

{indent}Some description.
{indent}"""


@pytest.mark.parametrize("version", ["3.7.0", "3.7.1", "3.6.2"])
def test_requires_geos_ok(version, mocked_geos_version):
    wrapped = requires_geos(version)(func)
    assert wrapped is func


@pytest.mark.parametrize("version", ["3.7.2", "3.8.0", "3.8.1"])
def test_requires_geos_not_ok(version, mocked_geos_version):
    wrapped = requires_geos(version)(func)
    with pytest.raises(shapely.errors.UnsupportedGEOSVersionError):
        wrapped()

    assert wrapped.__doc__ == expected_docstring.format(version=version, indent=" " * 4)


@pytest.mark.parametrize("version", ["3.6.0", "3.8.0"])
def test_requires_geos_doc_build(version, mocked_geos_version, sphinx_doc_build):
    """The requires_geos decorator always adapts the docstring."""
    wrapped = requires_geos(version)(func)

    assert wrapped.__doc__ == expected_docstring.format(version=version, indent=" " * 4)


@pytest.mark.parametrize("version", ["3.6.0", "3.8.0"])
def test_requires_geos_method(version, mocked_geos_version, sphinx_doc_build):
    """The requires_geos decorator adjusts methods docstrings correctly"""
    wrapped = requires_geos(version)(SomeClass.func)

    assert wrapped.__doc__ == expected_docstring.format(version=version, indent=" " * 8)


@multithreading_enabled
def set_first_element(value, *args, **kwargs):
    for arg in chain(args, kwargs.values()):
        if hasattr(arg, "__setitem__"):
            arg[0] = value
            return arg


def test_multithreading_enabled_raises_arg():
    arr = np.empty((1,), dtype=object)

    # set_first_element cannot change the input array
    with pytest.raises(ValueError):
        set_first_element(42, arr)

    # afterwards, we can
    arr[0] = 42
    assert arr[0] == 42


def test_multithreading_enabled_raises_kwarg():
    arr = np.empty((1,), dtype=object)

    # set_first_element cannot change the input array
    with pytest.raises(ValueError):
        set_first_element(42, arr=arr)

    # writable flag goes to original state
    assert arr.flags.writeable


def test_multithreading_enabled_preserves_flag():
    arr = np.empty((1,), dtype=object)
    arr.flags.writeable = False

    # set_first_element cannot change the input array
    with pytest.raises(ValueError):
        set_first_element(42, arr)

    # writable flag goes to original state
    assert not arr.flags.writeable


@pytest.mark.parametrize(
    "args,kwargs",
    [
        ((np.empty((1,), dtype=float),), {}),  # float-dtype ndarray is untouched
        ((), {"a": np.empty((1,), dtype=float)}),
        (([1],), {}),  # non-ndarray is untouched
        ((), {"a": [1]}),
        ((), {"out": np.empty((1,), dtype=object)}),  # ufunc kwarg 'out' is untouched
        (
            (),
            {"where": np.empty((1,), dtype=object)},
        ),  # ufunc kwarg 'where' is untouched
    ],
)
def test_multithreading_enabled_ok(args, kwargs):
    result = set_first_element(42, *args, **kwargs)
    assert result[0] == 42

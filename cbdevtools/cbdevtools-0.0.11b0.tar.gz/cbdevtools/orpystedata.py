#!/usr/bin/env python3

###
# This module simplifies the use of path::``PEUF`` files for datas used
# to achieve unit tests (see the project ¨orpyste).
###


from typing import *

from pathlib import Path
from pytest  import fixture

from orpyste.data import ReadBlock


###
# prototype::
#     :action: this function is a fixture for ¨pytest yielding a ready-to-use
#              data dictionary used to acheive some tests.
#              It also finalizes the cleaning of ¨orpyste extra files in case
#              of problem.
#
#     :see: build_datas_block
#
#
# note::
#     The "intuitive" ready-to-use dictionary is build via the call of
#     ``mydict("std nosep nonb")`` (see ¨orpyste).
#
#
# refs::
#    * https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session
#    * https://docs.pytest.org/en/6.2.x/fixture.html#factories-as-fixtures
###

@fixture(scope = "session")
def peuf_fixture() -> None:
    datas_build = []

###
# This internal function always has the same signature as the function
# ``build_datas_block``.
###
    def _make_peuf_datas(*args, **kwargs) -> None:
        datas_build.append(
            datas := build_datas_block(*args, **kwargs)
        )

        datas.build()

        return datas.mydict("std nosep nonb")

    yield _make_peuf_datas

    for datas in datas_build:
        datas.remove_extras()


###
# prototype::
#     file : just use the magic constant ``__file__`` when calling this
#            function from a testing file.
#
#     :return: an instance of ``ReadBlock`` associated to a path::``peuf``
#              file automatically named.
#
#
# warning::
#     The name of the path::``peuf`` file is obtained by removing the prefix
#     path::``test_`` from the name of the testing file (see the ¨tech ¨doc
#     of ``peuf_fixture`` for a concrete example).
###
def build_datas_block(
    file: str,
) -> ReadBlock:
    file    = Path(file)
    filedir = file.parent

    whatistested = file.stem
    whatistested = whatistested.replace('test_', '')

    return ReadBlock(
        content = filedir / f'{whatistested}.peuf',
        mode    = {"keyval:: =": ":default:"}
    )

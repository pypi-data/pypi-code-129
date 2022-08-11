#!/usr/bin/env python3

###
# This module allows to work with selective version of the standard ``dir(obj)``
# of an object.
###


from typing import (
    Any,
    List,
)

from re import (
    compile as re_compile,
    Pattern as re_Pattern,
)


PATTERN_UNDERSCORE = re_compile('_.*')

###
# prototype::
#     obj      : any ¨python object.
#     toignore : a list of forbidden matching defined via regexes
#
#     :return: the list of methods given by ``dir(obj)`` after removing
#              the unwanted names specified by the optional parameters
#              ``nounderscore``, ``notstartwith`` and ``toignore``.
###
def shortdir(
    obj     : Any,
    toignore: List[re_Pattern] = [PATTERN_UNDERSCORE],
) -> List[str]:
    if not toignore:
        return dir(obj)

    shortdirobj = []

    for name in dir(obj):
        if any(
            p.fullmatch(name)
            for p in toignore
        ):
            continue

        shortdirobj.append(name)

    return shortdirobj

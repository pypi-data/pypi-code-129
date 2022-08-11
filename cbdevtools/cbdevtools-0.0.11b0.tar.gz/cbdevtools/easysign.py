#!/usr/bin/env python3

###
# This module gives the possibility to obtain an easy-to-use dictinoary giving
# ¨infos about the signature of a callable object.
#
#
# note::
#    The hard job is done by the excellent ``inspect.signature``.
###

from typing import (
    Any,
    Callable,
    Dict,
    # List,
    Union,
)

from inspect import signature


# Some useful tags.
TAG_PARAMS   = 'params'
TAG_OPTIONAL = 'optional'
TAG_RETURN   = 'return'

TAG_TYPING  = 'typing'
TAG_DEFAULT = 'default'


###
# prototype::
#     onetype : a "full" typing ¨info that can be empty (in case of typing
#               was used in the original ¨src code).
#
#     :return: a minimalistic typing ¨info, or
#              None if no typing ¨info was given.
###
def cleantype(onetype: str) -> Union[None, str]:
    onetype = onetype.strip()

# Short typing info.
    for toremove in [
        "typing.",
        "<class '",
        "'>"
    ]:
        onetype = onetype.replace(toremove, "")

# No typing info?
    if(
        onetype == 'inspect._empty'
        or
        onetype == ''
    ):
        onetype = None

# Nothing left to do.
    return onetype


###
# prototype::
#     onecallable : any callable object (one function, or one method of
#                   a class)
#
#     :return: a dictionary giving all the ¨infos about the siganture of
#              ``onecallable``.
#
#
# warning::
#     When nothing has been indicated in the original code, the value
#     ``None`` is used.
###
def easysign(onecallable: Callable) -> Dict[str, Any]:
# Thanks for the hard job done by ``signature``.
    sign = signature(onecallable)

# An easier version of the signature (at least for me).
    easysign = {
        TAG_PARAMS  : {},
        TAG_OPTIONAL: [],
        TAG_RETURN  : cleantype(str(sign.return_annotation)),
    }

    for param, annotation in sign.parameters.items():
        _, _, param_type_default = str(annotation).partition(':')

        param_type, *param_default = param_type_default.split('=')

        if param_default:
            param_default = param_default[0].strip()

            easysign[TAG_OPTIONAL].append(param)

        else:
            param_default = None

        easysign[TAG_PARAMS][param] = {
            TAG_TYPING : cleantype(param_type),
            TAG_DEFAULT: param_default,
        }

# We can deliver our so little job.
    return easysign

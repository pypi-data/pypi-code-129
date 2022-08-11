#!/usr/bin/env python3


"""
"""  """

This file is part of python-etask.

python-etask is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 3.

python-etask is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with python-etask.  If not, see <https://www.gnu.org/licenses/>.

Copyright (c) 2022, Maciej Barć <xgqt@riseup.net>
Licensed under the GNU GPL v3 License
SPDX-License-Identifier: GPL-3.0-only
"""


from sys import version_info

from . import __description__, __epilog__, __version__


def pinfo(emacs, pprint):
    """!
    Print short info about the program.

    @param emacs: a Emacs object
    @param emacs: a Pprint object
    """

    python_version = f"{version_info.major}.{version_info.minor}"

    try:
        emacs_version = emacs.get_version()
    except RuntimeError:
        emacs_version = "unknown"

    print(
        f"{pprint.bright}{pprint.green}ETask{pprint.reset}, " +
        f"{__description__}," +
        " " +
        f"version {pprint.green}{__version__}{pprint.reset}, " +
        f"running on {pprint.bright}{pprint.blue}Python" +
        " " +
        f"{python_version}{pprint.reset} " +
        f"and {pprint.bright}{pprint.magenta}GNU Emacs {emacs_version}" +
        f"{pprint.reset}"
    )
    print(__epilog__)

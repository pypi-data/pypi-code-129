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


import colorama


colorama.init(autoreset=True)


class Pprint:
    """!
    The pretty-printing class.
    """

    def __init__(self, color):
        if color:
            self.blue = colorama.Fore.BLUE
            self.green = colorama.Fore.GREEN
            self.magenta = colorama.Fore.MAGENTA
            self.red = colorama.Fore.RED
            self.white = colorama.Fore.WHITE
            self.yellow = colorama.Fore.YELLOW
            self.bright = colorama.Style.BRIGHT
            self.reset = colorama.Fore.RESET + colorama.Style.RESET_ALL
        else:
            self.blue = ""
            self.green = ""
            self.magenta = ""
            self.red = ""
            self.white = ""
            self.yellow = ""
            self.bright = ""
            self.reset = ""

    def _print(self, symbol, color, string):
        """!
        Print helper.

        @param symbol: string to indicate the message (eg. "!")
        @param string: color to indicate the message (eg. red)
        @param string: string to print (eg. "message")
        """

        print(
            "  " +
            f"{self.bright}{self.white}" +
            f"[{color}{symbol * 3}{self.white}]" +
            f"{self.reset}:" +
            " " +
            f"{string}")

    def debug(self, string):
        """!
        Debug print.

        @param string: string to print
        """

        self._print("*", self.yellow, string)

    def info(self, string):
        """!
        Info print.

        @param string: string to print
        """

        self._print(".", self.green, string)

    def warning(self, string):
        """!
        Warning print.

        @param string: string to print
        """

        self._print("!", self.red, string)

    def std(self, std_lines):
        """!
        Helper to print "stdout" and "stderr" from std_lines.

        @param: dict of lines to print
        """

        for stdout_line in std_lines["stdout"]:
            if stdout_line != "":
                self.info(stdout_line)

        for stdout_line in std_lines["stderr"]:
            if stdout_line != "":
                self.warning(stdout_line)

    def args(self, namespace):
        """!
        Pretty-print args from a given namespace.

        @param: args namespace to print
        """

        for option, value in vars(namespace).items():

            if value is True:
                color = self.green
            elif value is False:
                color = self.red
            elif value is None:
                color = self.blue
            else:
                color = self.white

            self.debug(
                f"{self.bright}{self.white}{option}{self.reset}:" +
                " " +
                f"{color}{value}{self.reset}")

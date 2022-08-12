#!/usr/bin/env python3
# Copyright (c) 2022 4ndrs <andres.degozaru@gmail.com>
# SPDX-License-Identifier: MIT
# pylint: disable=missing-module-docstring
import sys
from os import getpid
from subprocess import check_output, CalledProcessError  # nosec


def main():
    """Change the status of a given process (or a group of processes) sending
    SIGSTOP/SIGCONT.

        Usage:  psus firefox suspend
                psus firefox continue
    The script will search for processes with the string in the first
    command-line argument and execute the action specified in the second
    command-line argument."""
    if len(sys.argv) < 2:
        print("Arguments must be given to proceed", file=sys.stderr)
        sys.exit(1)
    if len(sys.argv) < 3:
        print("An action must be given to proceed", file=sys.stderr)
        sys.exit(2)

    if sys.argv[2] != "suspend" and sys.argv[2] != "continue":
        print(
            f"Unrecognized action: {sys.argv[2]}\n"
            "The action can be either 'suspend' or 'continue'",
            file=sys.stderr,
        )
        sys.exit(3)
    else:
        process_txt = sys.argv[1]
        suspend = "suspend" in sys.argv[2]

    try:
        pids = (
            check_output(["pgrep", "-f", process_txt])  # nosec
            .decode()
            .strip()
            .split("\n")
        )
    except CalledProcessError:  # this will never raise because of our pid
        print("No processes found", file=sys.stderr)
        sys.exit(4)

    our_pid = str(getpid())
    if our_pid in pids:
        pids.remove(our_pid)

    for pid in pids:
        if suspend:
            check_output(["kill", "-SIGSTOP", pid])
        else:
            check_output(["kill", "-SIGCONT", pid])

    print(f"Signaled {len(pids)} process", end="")
    if len(pids) != 1:  # n < 1 needed for CalledProcessError not being raised
        print("es")
    else:
        print()


if __name__ == "__main__":
    main()

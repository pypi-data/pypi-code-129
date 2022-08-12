#!/usr/bin/env python3
# Copyright (c) 2022 4ndrs <andres.degozaru@gmail.com>
# SPDX-License-Identifier: MIT
"""A script to make cropping easy when ffmpeg'ing.
   Needs slop, xdotool, and xwininfo.

   Usage: ffmpeg -i input -vf crop=$(slopping) output

   To generate a PIL.Image crop tuple, pass 'pil' as argument: slopping pil"""

from sys import argv
import slopping


def main():
    """Prints the cropping coordinates to the screen"""
    pil = "pil" in argv

    crop = slopping.crop("pil" if pil else "ffmpeg")
    separator = ", " if pil else ":"

    for i, num in enumerate(crop):
        print(num, end="")
        if i < 3:
            print(separator, end="")


if __name__ == "__main__":
    main()

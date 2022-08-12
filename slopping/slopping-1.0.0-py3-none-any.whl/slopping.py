# Copyright (c) 2022 4ndrs <andres.degozaru@gmail.com>
# SPDX-License-Identifier: MIT
# pylint: disable=missing-module-docstring
from subprocess import check_output  # nosec
import re


def crop(argv="ffmpeg"):
    """Returns cropping coordinates as a tuple, argv can be either "ffmpeg" or
    "pil"."""
    pil = "pil" in argv

    crop_ = check_output(["slop", "-f", "%w %h %x %y"]).decode()
    crop_ = tuple(int(n) for n in crop_.split())  # (w, h, x, y)

    # The mouse pointer needs to be hovering the video we are cropping
    window_id = check_output(["xdotool", "getmouselocation", "--shell"])
    window_id = re.search(rb".*WINDOW=(\d+)", window_id).groups()[0]

    window_xy = check_output(["xwininfo", "-id", window_id]).decode()
    window_xy = tuple(
        int(n)
        for n in re.search(
            r"Absolute.*X:\s+([-]?\d+).*Absolute.*Y:\s+([-]?\d+)",
            window_xy,
            re.DOTALL,
        ).groups()
    )

    crop_xy = crop_[2:]

    # CROP_X - WINDOW_X, CROP_Y - WINDOW_Y
    crop_xy = tuple(c - w for c, w in zip(crop_xy, window_xy))
    crop_ = crop_[:2] + crop_xy

    if pil:
        # RIGHT_X = CROP_X + CROP_WIDTH, RIGHT_Y = CROP_Y + CROP_HEIGHT
        # CROP_X, CROP_Y, RIGHT_X, RIGHT_Y
        crop_ = crop_[2:] + (crop_[0] + crop_[2], crop_[1] + crop_[3])

    return crop_

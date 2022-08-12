# -*- coding: utf-8 -*-
#
# Copyright (c) 2022~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from typing import *
import hashlib
import os

def get_gcid_digest(fp, fp_size: int, *, progress_callback=None):
    '''
    Calc GCID from `fp`.
    '''

    if progress_callback is None:
        progress_callback = lambda _1, _2: None

    # modified from https://binux.blog/2012/03/hash_algorithm_of_xunlei/

    h = hashlib.sha1()

    piece_size = 0x40000
    while fp_size / piece_size > 0x200 and piece_size < 0x200000:
        piece_size = piece_size << 1

    buf = bytearray(piece_size)  # Reusable buffer to reduce allocations.
    buf_view = memoryview(buf)
    read_size_sum = 0
    while read_size := fp.readinto(buf):
        read_size_sum += read_size
        if read_size_sum > fp_size:
            raise ValueError('visit unexpected data.')
        h.update(hashlib.sha1(buf_view[:read_size]).digest())
        progress_callback(read_size_sum, fp_size)

    if fp_size != read_size_sum:
        raise ValueError('stream end too early.')

    return h.digest()

def get_file_gcid_digest(path: str, *, progress_callback=None):
    '''
    Calc GCID from `path`.
    '''
    with open(path, 'rb') as fp:
        return get_gcid_digest(fp, os.path.getsize(path),
            progress_callback=progress_callback)

__all__ = [
    'get_gcid_digest',
    'get_file_gcid_digest'
]

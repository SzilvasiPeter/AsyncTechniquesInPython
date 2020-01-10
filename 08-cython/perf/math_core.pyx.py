from libc.math cimport sqrt

import cython
from Cython.Shadow import nogil


def do_math(start: cython.int = 0, num: cython.int = 10):
    pos: cython.int = start
    k_sq: cython.int = 1000 * 1000
    with nogil:
        while pos < num:
            pos += 1
            dist = math.sqrt((pos - k_sq) * (pos - k_sq))

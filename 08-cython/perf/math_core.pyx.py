from libc.math cimport sqrt

import cython
from Cython.Shadow import nogil


def do_math(start: cython.float = 0, num: cython.float = 10):
    pos: cython.float = start
    k_sq: cython.float = 1000 * 1000

    with nogil:
        while pos < num:
            pos += 1
            dist = math.sqrt((pos - k_sq) * (pos - k_sq))

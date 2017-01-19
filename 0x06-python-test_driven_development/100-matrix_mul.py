#!/usr/bin/python3
"""
This is the "matrix_mul" module.

The matrix_mul module supplies a simple function that does matrix multiplication
"""


def matrix_mul(m_a, m_b):
    n_mtrx = []
    for i in m_a:
        mtrx = []
        indx = 0
        j = 0
        mul = 0
        for k in m_b:
            mul += i[j] * k[indx]
            print("", j, k[indx], mul)
            j += 1
            mtrx.append(mul)
        indx += 1
        n_mtrx.append(mtrx)
    return n_mtrx

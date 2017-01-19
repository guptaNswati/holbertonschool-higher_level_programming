#!/usr/bin/python3
"""
This is the "matrix_mul" module.

The matrix_mul module supplies a simple function that does matrix multiplication
"""


def matrix_mul(m_a, m_b):
    if not m_a:
        raise ValueError("m_a can't be empty")
    if not m_b:
        raise ValueError("m_b can't be empty")
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
         raise TypeError("m_b must be a list")
    if not isinstance(m_a[0], list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b[0], list):
        raise TypeError("m_b must be a list")
    row_len = len(m_a[0])
    for i in m_a:
        if not len(i) == row_len:
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError("m_a should contain only integers or floats")
    row_len = len(m_b[0])
    for i in m_b:
        if not len(i) == row_len:
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError("m_b should contain only integers or floats")

    if not len(m_a[0]) == len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    mtrx = [[0 for vertcl in range(len(m_b[0]))] for horintl in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                mtrx[i][j] += m_a[i][k] * m_b[k][j]
    return mtrx

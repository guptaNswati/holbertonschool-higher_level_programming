#!/usr/bin/python3
"""
This is the "lazy_matrix_mul" module.

The lazy_matrix_mul module does matrix multiplication using numpy.dot
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
       Takes in two Matrix and Multiplies them
       Return: a new matrix
    """
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
    m_c = np.dot(m_a, m_b)
    return m_c

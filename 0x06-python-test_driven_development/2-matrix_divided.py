#!/usr/bin/python3
"""
This is the "matrix_divided" module.

The matrix_divided module supplies a simple function that divides all elements
of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide elements of matrix and return a new matrix.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists)\
        of integers/floats")
    if not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists)\
         of integers/floats")
    row_len = len(matrix[0])
    n_matrx = []
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
        if not len(i) == row_len:
            raise TypeError("Each row of the matrix must have the same size")
        m_row = []
        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
                of integers/floats")
            m_row.append(round(j/div, 2))
        n_matrx.append(m_row)
    return n_matrx

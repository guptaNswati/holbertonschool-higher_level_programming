#!/usr/bin/python3
"""
This is the "matrix_divided" module.

The matrix_divided module supplies a simple function that divides all elements
of a matrix.
"""


def matrix_divided(matrix, div):
    """Divide elements of matri and return new matrix.
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("divisor must be an integer or float")
    row_len = len(matrix[0])
    n_matrx = []
    for i in matrix:
        if not len(i) == row_len:
            raise TypeError("matrix must have each row with the same size")
        m_row = []
        for j in i:
            if not (isinstance(j, int) or isinstance(j, float)):
                raise TypeError("matrix must be a matrix \
                (array of arrays of integers/floats)")
            m_row.append(round(j/div, 2))
        n_matrx.append(m_row)
    return n_matrx


if __name__ == '__main__':
    doctest.testfile('/2-matrix_divided.txt')

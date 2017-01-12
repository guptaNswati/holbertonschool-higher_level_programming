#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrs = []
    if matrix:
        for i in matrix:
            col = []
            for j in i:
                col.append(j * j)
            sqrs.append(col)
    return sqrs

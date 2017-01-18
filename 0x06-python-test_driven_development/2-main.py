#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [],
    []
]
print(matrix_divided(-3, -2))
print(matrix_divided("h", 3))
print(matrix_divided("s", "h"))
print(matrix_divided([1, 2, 3], 2))
print(matrix_divided([[1], [1]], 0))
print(matrix_divided(None, 1))
print(matrix_divided({5: "Holbrtn"}, 3))
print(matrix_divided(2, {1, 2, 3}))

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for i in matrix:
        for j in i:
            matrix[i][j] = matrix[i][j] ** 2
    return matrix

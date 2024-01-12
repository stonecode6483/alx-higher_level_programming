#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
    matrix (list): 2-dimensional array.
    Returns:
    list: New matrix with each value being the square of the input.
    """
    # Create a new matrix with the same size as the input matrix
    result_matrix = [[0 for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2
            return new_matrix

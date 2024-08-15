#!/usr/bin/python3
"""
This module provides a function to rotate a 2D matrix 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates an n x n 2D matrix 90 degrees clockwise in place.
    
    Args:
        matrix (list of list of int): The matrix to be rotated.
        
    Returns:
        None: The matrix is rotated in place.
    """
    n = len(matrix)

    for i in range(n // 2):
        for j in range(i, n - i - 1):
            # Save the top element
            top = matrix[i][j]

            # Move the left element to the top
            matrix[i][j] = matrix[n - j - 1][i]

            # Move the bottom element to the left
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]

            # Move the right element to the bottom
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]

            # Assign the top element to the right
            matrix[j][n - i - 1] = top

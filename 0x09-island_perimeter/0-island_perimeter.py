#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an island
in a grid of water and land cells.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid of water and land cells with no lakes.
    """
    perimeter = 0
    if type(grid) != list:
        return 0
    num_rows = len(grid)
    for row_index, row in enumerate(grid):
        num_cols = len(row)
        for col_index, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                row_index == 0 or (len(grid[row_index - 1]) > col_index and grid[row_index - 1][col_index] == 0),
                col_index == num_cols - 1 or (num_cols > col_index + 1 and row[col_index + 1] == 0),
                row_index == num_rows - 1 or (len(grid[row_index + 1]) > col_index and grid[row_index + 1][col_index] == 0),
                col_index == 0 or row[col_index - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter

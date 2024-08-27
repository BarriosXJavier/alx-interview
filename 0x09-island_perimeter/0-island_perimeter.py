#!/usr/bin/python3
"""
This module contains a function to calculate the perimeter of an island
in a grid of water and land cells.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid of
    water and land cells with no lakes.
    """
    perimeter = 0
    if not isinstance(grid, list):
        return 0
    num_rows = len(grid)
    for row_idx, row in enumerate(grid):
        num_cols = len(row)
        for col_idx, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                row_idx == 0 or (len(grid[row_idx - 1]) > col_idx and
                                 grid[row_idx - 1][col_idx] == 0),
                col_idx == num_cols - 1 or (num_cols > col_idx + 1 and
                                            row[col_idx + 1] == 0),
                row_idx == num_rows - 1 or (len(grid[row_idx + 1]) >
                                            col_idx and
                                            grid[row_idx + 1][col_idx] == 0),
                col_idx == 0 or row[col_idx - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter

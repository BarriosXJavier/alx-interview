#!/usr/bin/env python3
"""
This module contains a function to calculate the perimeter of an island
in a grid of water and land cells.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    The grid is a list of lists where 0 represents water and 1 represents land.
    The island is surrounded by water and there are no lakes within the island.

    Args:
        grid (list of list of int): A list of lists representing the grid.

    Returns:
        int: The perimeter of the island in the grid.
    """
    if not grid:
        return 0

    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Each land cell initially adds 4 to the perimeter
                perimeter += 4
                # Subtract 2 for each adjacent land cell above
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                # Subtract 2 for each adjacent land cell to the left
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter

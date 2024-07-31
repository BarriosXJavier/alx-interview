#!/usr/bin/python3
"""N queens solution finder module."""
import sys

solutions = []
"""The list of possible solutions to the N queens problem."""
board_size = 0
"""The size of the chessboard."""
positions = None
"""The list of possible positions on the chessboard."""

def get_input():
    """Retrieves and validates this program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global board_size
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size

def is_attacking(pos1, pos2):
    """Checks if the positions of two queens are in an attacking mode.

    Args:
        pos1 (list or tuple): The first queen's position.
        pos2 (list or tuple): The second queen's position.

    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    return pos1[0] == pos2[0] or pos1[1] == pos2[1] or abs(pos1[0] - pos2[0]) == abs(pos1[1] - pos2[1])

def solution_exists(candidate_solution):
    """Checks if a candidate solution exists in the list of solutions.

    Args:
        candidate_solution (list of lists of integers): A candidate solution.

    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for existing_solution in solutions:
        if all(any(c_pos[0] == e_pos[0] and c_pos[1] == e_pos[1] for e_pos in existing_solution) for c_pos in candidate_solution):
            return True
    return False

def find_solutions(row, current_solution):
    """Builds a solution for the n queens problem.

    Args:
        row (int): The current row in the chessboard.
        current_solution (list of lists of integers): The current valid positions.
    """
    global solutions, board_size
    if row == board_size:
        if not solution_exists(current_solution):
            solutions.append(current_solution.copy())
        return
    for col in range(board_size):
        candidate_position = [row, col]
        if not any(is_attacking(candidate_position, existing_position) for existing_position in current_solution):
            current_solution.append(candidate_position)
            find_solutions(row + 1, current_solution)
            current_solution.pop()

def solve_nqueens():
    """Gets the solutions for the given chessboard size."""
    global positions, board_size
    positions = [[i, j] for i in range(board_size) for j in range(board_size)]
    find_solutions(0, [])

board_size = get_input()
solve_nqueens()
for solution in solutions:
    print(solution)

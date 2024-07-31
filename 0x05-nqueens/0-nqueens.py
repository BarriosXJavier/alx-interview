#!/usr/bin/python3

"""
Solves the N-Queens problem.

The N-Queens problem is a classic problem in computer science where the goal is to place N queens on an NxN chessboard such that no two queens attack each other.

Usage:
    nqueens N

Where N is the size of the chessboard.

Example:
    nqueens 4
"""

import sys

def print_usage_and_exit(message):
    """
    Prints an error message and exits the program.

    Args:
        message (str): The error message to print.
    """
    print(message)
    sys.exit(1)

def is_valid(board, row, col, N):
    """
    Checks if a queen can be placed at the given position on the board.

    Args:
        board (list): The current state of the board.
        row (int): The row to check.
        col (int): The column to check.
        N (int): The size of the board.

    Returns:
        bool: True if a queen can be placed at the given position, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i] == j:
            return False

    return True

def solve_nqueens(N, row, board, solutions):
    """
    Recursively solves the N-Queens problem.

    Args:
        N (int): The size of the board.
        row (int): The current row to solve.
        board (list): The current state of the board.
        solutions (list): A list to store the solutions.

    Returns:
        None
    """
    if row == N:
        solutions.append(board[:])
        return

    for col in range(N):
        if is_valid(board, row, col, N):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            board[row] = -1

def print_solutions(solutions):
    """
    Prints the solutions to the N-Queens problem.

    Args:
        solutions (list): A list of solutions.

    Returns:
        None
    """
    for solution in solutions:
        print("[", end="")
        print(", ".join(f"[{i}, {solution[i]}]" for i in range(len(solution))), end="")
        print("]")

def main():
    """
    The main entry point of the program.

    Returns:
        None
    """
    if len(sys.argv) != 2:
        print_usage_and_exit("Usage: nqueens N")

    try:
        N = int(sys.argv[1])
    except ValueError:
        print_usage_and_exit("N must be a number")

    if N < 4:
        print_usage_and_exit("N must be at least 4")

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
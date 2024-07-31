#!/usr/bin/python3
""" N Queens challenge """
import sys


def print_board(board, n):
    """Print allocated positions to the queen"""
    b = []
    for i in range(n):
        b.append([i, board[i]])
    print(b)


def is_position_safe(board, i, j):
    """Checks if the position is safe for the queen"""
    for r in range(i):
        if board[r] == j or \
           board[r] - r == j - i or \
           board[r] + r == j + i:
            return False
    return True


def safe_positions(board, row, n):
    """Find all safe positions where the queen can be allocated"""
    if row == n:
        print_board(board, n)
    else:
        for j in range(n):
            if is_position_safe(board, row, j):
                board[row] = j
                safe_positions(board, row + 1, n)


def create_board(size):
    """Generates the board"""
    return [-1] * size


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = create_board(n)
    safe_positions(board, 0, n)

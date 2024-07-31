#!/usr/bin/python3
""" Script to solve the n-queen challenge"""
import sys


def is_safe(board, row, col, n):
    """Checks if it is safe to place a queen at board[row][col]"""
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for queens in the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n, solutions):
    """Solves the N-Queens problem using backtracking"""
    if col >= n:
        solutions.append([row[:] for row in board])
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_n_queens(board, col + 1, n, solutions)
            board[i][col] = 0


def format_solution(board):
    """Formats the solution to the required output"""
    solution = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    return solution


def print_solutions(solutions):
    """Prints all solutions to the N-Queens problem"""
    for solution in solutions:
        formatted_solution = format_solution(solution)
        print(formatted_solution)


def main():
    """Main function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    n = sys.argv[1]

    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_n_queens(board, 0, n, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    main()

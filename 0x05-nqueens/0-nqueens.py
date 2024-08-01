import sys

"""
The N queens challenge
"""

def is_safe(board, row, col, n):
    """
    Check if a queen can be placed on board at (row, col).

    Args:
        board (list): The board configuration.
        row (int): The current row to place the queen.
        col (int): The current column to place the queen.
        n (int): The size of the board.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(row):
        # Check if there is a queen in the same column or diagonals
        if (board[i] == col or
            board[i] - i == col - row or
            board[i] + i == col + row):
            return False
    return True

def solve_n_queens(n, row, board, solutions):
    """
    Solve the N Queens problem using backtracking.

    Args:
        n (int): The size of the board.
        row (int): The current row to place a queen.
        board (list): The board configuration.
        solutions (list): A list to store all possible solutions.

    Returns:
        None
    """
    if row == n:
        # If all queens are placed, add the solution to the list
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_n_queens(n, row + 1, board, solutions)

def print_solutions(solutions, n):
    """
    Print all solutions in the required format.

    Args:
        solutions (list): A list of all solutions.
        n (int): The size of the board.

    Returns:
        None
    """
    for solution in solutions:
        # Format each solution as a list of [row, col] pairs
        formatted_solution = [[i, solution[i]] for i in range(n)]
        print(formatted_solution)

def main():
    """
    Main function to parse command line arguments and solve the N Queens problem.

    Exits with status 1 in case of incorrect usage or invalid input.
    """
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

    solutions = []
    solve_n_queens(n, 0, [-1] * n, solutions)
    print_solutions(solutions, n)

if __name__ == "__main__":
    main()

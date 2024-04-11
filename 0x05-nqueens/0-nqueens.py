#!/usr/bin/python3
"""N-Queens Challenge"""

import sys


def is_safe(placed_queens, r, c):
    """Check if it's safe to place a queen at (r, c)"""
    for row, col in placed_queens:
        if col == c or col + (r - row) == c or col - (r - row) == c:
            return False
    return True


def find_solutions(n):
    """Find all solutions to the N-Queens problem for an NxN board"""
    solutions = []
    placed_queens = []

    def backtrack(r):
        if r == n:
            solutions.append(placed_queens[:])
            return

        for c in range(n):
            if is_safe(placed_queens, r, c):
                placed_queens.append([r, c])
                backtrack(r + 1)
                placed_queens.pop()

    backtrack(0)
    return solutions


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = find_solutions(n)

    for solution in solutions:
        print(solution)

#!/usr/bin/python3
import sys
"""
This is a nQueens class.
The nQueens class solve the nQueen puzzle using backtracking.
"""


class nQueens:
    """
    Check if a given column is valid
    """
    def isValid(self, i, k, solCols):
        for l in range(i):
            if solCols[l] == k:
                return False
            if abs(solCols[l] - k) == (i - l):
                return False
        return True

    """
    Find all possible solutions recursivley for a given row.
    """
    def solve(self, row, N, solCols):
        if row == N:
            print("[", end="")
            for i in range(N):
                print("[{:d}, {:d}]".format(i, solCols[i]), end="")
                if i < N - 1:
                    print(", ", end="")
            print("]")
            return
        for i in range(N):
            if self.isValid(row, i, solCols):
                solCols[row] = i
                self.solve(row+1, N, solCols)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    else:
        try:
            N = int(sys.argv[1])
        except:
            print("N must be a number")
            exit(1)
        if N < 4:
            print("N must be at least 4")
            exit(1)
        nQueen_bcktrck = nQueens()
        nQueen_bcktrck.solve(0, N, [None for i in range(N)])

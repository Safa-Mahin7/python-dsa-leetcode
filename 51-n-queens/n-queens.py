class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                # Place queen
                cols.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Move to next row
                backtrack(r + 1)

                # Remove queen (backtrack)
                cols.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res
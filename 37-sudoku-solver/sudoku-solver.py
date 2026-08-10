class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # 1. Pre-populate existing numbers and track empty cells
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    box_idx = (r // 3) * 3 + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                else:
                    empty_cells.append((r, c))

        # 2. Optimized Backtracking
        def backtrack(index: int) -> bool:
            if index == len(empty_cells):
                return True

            r, c = empty_cells[index]
            box_idx = (r // 3) * 3 + (c // 3)

            for digit in "123456789":
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[box_idx]:
                    # Place digit
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[box_idx].add(digit)

                    if backtrack(index + 1):
                        return True

                    # Backtrack
                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[box_idx].remove(digit)

            return False

        backtrack(0)
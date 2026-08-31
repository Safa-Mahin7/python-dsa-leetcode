class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        
        while num <= n * n:
            # Fill top row (left to right)
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1
            
            # Fill right column (top to bottom)
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1
            
            # Fill bottom row (right to left)
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1
            
            # Fill left column (bottom to top)
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1
            
        return matrix
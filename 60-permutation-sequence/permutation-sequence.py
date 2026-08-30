import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of numbers to get candidates from
        numbers = [str(i) for i in range(1, n + 1)]
        
        # Convert k to 0-based index
        k -= 1
        
        # Precompute factorials: (n-1)! down to 0!
        factorial = math.factorial(n - 1)
        
        result = []
        for i in range(n - 1, 0, -1):
            # Determine the index of the next number to pick
            index = k // factorial
            result.append(numbers.pop(index))
            
            # Update k and calculate the next factorial
            k %= factorial
            factorial //= i
            
        # Append the remaining single digit
        result.append(numbers[0])
        
        return "".join(result)
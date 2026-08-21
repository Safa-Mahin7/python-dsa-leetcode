class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Edge case: if either number is "0", product is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        len1, len2 = len(num1), len(num2)
        # Result array can have at most (len1 + len2) digits
        result = [0] * (len1 + len2)

        # Multiply each digit of num1 with each digit of num2 from right to left
        for i in range(len1 - 1, -1, -1):
            digit1 = ord(num1[i]) - ord("0")
            for j in range(len2 - 1, -1, -1):
                digit2 = ord(num2[j]) - ord("0")

                # The product of digits at indices i and j contributes
                # to position i + j + 1 (and carries over to i + j)
                mul = digit1 * digit2
                p1, p2 = i + j, i + j + 1

                total = mul + result[p2]
                result[p2] = total % 10
                result[p1] += total // 10

        # Convert result array to string, skipping leading zeros
        start = 0
        while start < len(result) and result[start] == 0:
            start += 1

        return "".join(map(str, result[start:]))
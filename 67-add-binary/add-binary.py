class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1

        while i >= 0 or j >= 0 or carry:
            total = carry
            
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            
            # Append the sum modulo 2 (0 or 1)
            result.append(str(total % 2))
            # Compute new carry (1 if total >= 2 else 0)
            carry = total // 2

        # Reverse the array since we built the string backwards
        return "".join(reversed(result))
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        countT = Counter(t)
        window = {}
        
        have, need = 0, len(countT)
        res, res_len = [-1, -1], float("inf")
        l = 0
        
        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) + 1
            
            if char in countT and window[char] == countT[char]:
                have += 1
            
            while have == need:
                # Update smallest window result
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1
                
                # Pop from the left of window to minimize
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
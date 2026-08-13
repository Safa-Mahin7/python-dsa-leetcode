class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr = 0
        p_ptr = 0
        star_idx = -1
        s_tmp_idx = -1
        
        while s_ptr < len(s):
            # 1. Matching characters or '?' wildcard
            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            # 2. Encountered '*' wildcard in pattern
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                s_tmp_idx = s_ptr
                p_ptr += 1  # Try matching 0 characters first
            # 3. Mismatch, but we saw a '*' earlier -> Backtrack
            elif star_idx != -1:
                p_ptr = star_idx + 1
                s_tmp_idx += 1
                s_ptr = s_tmp_idx
            # 4. Mismatch with no preceding '*'
            else:
                return False
        
        # Check remaining characters in pattern (must all be '*')
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len(p)
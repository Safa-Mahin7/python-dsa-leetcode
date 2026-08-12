from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        
        for s in strs:
            # Sorted tuple acts as a unique key for all anagrams
            key = tuple(sorted(s))
            ans[key].append(s)
            
        return list(ans.values())
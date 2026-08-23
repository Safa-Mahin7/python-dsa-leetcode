class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0
        
        # We don't need to process the last element (len(nums) - 1)
        # as we are already at the destination when we reach or cross it.
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            
            #When we reach the boundary of the current jump,
            # we must make another jump.
            if i == current_end:
                jumps += 1
                current_end = farthest
                
        return jumps
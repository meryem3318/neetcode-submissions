class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i in range(len(nums)):
            # If your current position is beyond what you can reach, you're stuck
            if i > max_reach:
                return False
            
            # Update the furthest index you can reach from index i
            max_reach = max(max_reach, i + nums[i])
            
            # Early exit: if you can already reach or pass the last index
            if max_reach >= len(nums) - 1:
                return True
                
        return True
        
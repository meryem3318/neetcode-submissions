class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0
        
        for n in nums:
            # If currentSum becomes negative, reset it to 0 before adding n
            if currentSum < 0:
                currentSum = 0
            
            currentSum += n
            maxSum = max(maxSum, currentSum)
            
        return maxSum
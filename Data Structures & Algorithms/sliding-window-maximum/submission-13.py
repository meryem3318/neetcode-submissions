class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        temp = 0
        l, r = 0, (k-1)
        while r <= len(nums) - 1:
            for n in nums[l:r+1]:
                temp = max(temp, n)
            output.append(temp)
            l += 1
            r += 1
            temp = float("-inf")
        return output
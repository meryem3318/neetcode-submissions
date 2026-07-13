class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        m = (l + r) // 2
        for n in nums:
            for i in range(l, m+1):
                if nums[i] == target:
                    return i
                
            l = m
            m = len(nums) - 1
        return -1


                

        
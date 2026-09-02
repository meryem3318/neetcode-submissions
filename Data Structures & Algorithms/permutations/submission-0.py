class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]] # case where its empty

        perms = self.permute(nums[1:]) # we call permute on nums after first item
        res = []
        for p in perms: # we iterate through the rest of list
            for i in range(len(p) + 1):
                pcopy = p.copy() # why did we create a copy though
                pcopy.insert(i, nums[0]) # insert nums[0] at index i
                res.append(pcopy)
        return res


        
        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        # Keep 'l' static. It goes from 0 up to n-2.
        for l in range(0, n - 1):
            
            # The strategy: Scan ALL numbers to the right of 'l'
            # We use an inner pointer 'r'. We reset 'r' for every new 'l'.
            for r in range(l + 1, n):
                
                # Check the static number (l) against the scanning number (r)
                if nums[l] == nums[r]:
                    return nums[l]  # Found the duplicate!
        
        # If no duplicate is found (the problem guarantees one exists,
        # so this part is technically unreachable in normal usage).
        return -1



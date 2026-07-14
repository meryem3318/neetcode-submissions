class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            # 1. Check if we found the target
            if nums[mid] == target:
                return mid
            
            # 2. Check if the left half is normally sorted
            if nums[low] <= nums[mid]:
                # Is the target within the sorted left half?
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Search left
                else:
                    low = mid + 1   # Search right
                    
            # 3. Otherwise, the right half must be normally sorted
            else:
                # Is the target within the sorted right half?
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Search right
                else:
                    high = mid - 1  # Search left
                    
        # Target was not found in the array
        return -1
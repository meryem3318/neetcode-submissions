class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = nums1 + nums2
        new.sort()
        l = 0
        r = len(new) - 1
        if len(new) % 2 == 0:
            m = (l + r) // 2
            return (new[m] + new[m+1]) / 2
        else:
            m = (l + r) // 2
            return new[m]


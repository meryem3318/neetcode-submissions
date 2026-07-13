class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        res = high  

        while low <= high:
            k = (low + high) // 2
            
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k
            if total_hours <= h:
                res = k
                high = k - 1
            else:
                low = k + 1
                
        return res
import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heapify distances then pop coordinates as k decreases
        distances = [] 
        for x, y in points:
            dist = x**2 + y**2
            distances.append((dist, [x, y]))

        heapq.heapify(distances)

        res = []
        while k > 0:
            dist, point = heapq.heappop(distances)
            res.append(point)
            k -= 1

        return res


        

        
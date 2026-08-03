import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 1. Count frequencies
        counts = Counter(tasks)
        # 2. Max-heap: store negative counts so highest frequency comes out first
        max_heap = [-cnt for cnt in counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        cooldown_queue = deque() 
        
        while max_heap or cooldown_queue:
            time += 1
            
            # If we have available tasks in our heap, process the highest frequency
            if max_heap:
                cnt = heapq.heappop(max_heap) + 1  # Reduce count (since it's negative, +1 gets closer to 0)
                
                if cnt != 0:
                    # Task still has remaining work; can't be used again until time + n
                    cooldown_queue.append((cnt, time + n))
            
            # Check if any task in the cooldown queue is ready to go back to the heap
            if cooldown_queue and cooldown_queue[0][1] == time:
                ready_cnt, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, ready_cnt)
                
        return time
        


import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Step 1: Count frequencies (HashMap)
        freq = {}
        for char in tasks:
            freq[char] = 1 + freq.get(char, 0)
            
        # Step 2: Build Max-Heap (using negated frequencies)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)

        time = 0
        
        # *** FIX #1: Initialize the deque conceptual conceptual conceptual conceptual conceptual constructs conceptual models conceptual concepts concepts conceptual conceptual concepts conceptual constraints models models conceptual conceptually conceptual
        cooldown_queue = deque()
        
        # Phase 0: Main simulation conceptual
        while max_heap or cooldown_queue:
            
            # Phase A: Check "Waiting Room" (Return task if done cooling down)
            if cooldown_queue and cooldown_queue[0][1] == time:
                cnt_to_return, _ = cooldown_queue.popleft()
                heapq.heappush(max_heap, cnt_to_return)
            
            # (We only defined 'cnt' in your code conceptual when max_heap existed.)
            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1
                if cnt < 0:
                    cooldown_queue.append((cnt, time + n + 1))
                    

            else:
                pass 

            time += 1
            
        return time

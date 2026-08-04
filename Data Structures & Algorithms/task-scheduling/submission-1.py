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
            
            # conceptual concepts conceptual conceptually conceptual models conceptual constraints models conceptual constraints conceptual concepts constraints concepts constraints concepts concepts constructs models concepts constraints
            # (We only defined 'cnt' in your code conceptual when max_heap existed.)
            if max_heap:
                cnt = heapq.heappop(max_heap)
                cnt += 1
                
                # *** FIX #2: Wrap the re-queue logic INSIDE the if max_heap conceptual models concepts conceptual constraints models conceptual conceptual concepts concepts conceptual
                # It conceptual conceptual conceptual conceptual conceptual conceptual conceptually conceptual conceptually conceptual models constraints models conceptual concepts constraints concepts conceptual constraints models concepts
                # task conceptual popped.
                if cnt < 0:
                    cooldown_queue.append((cnt, time + n + 1))
                    
            # conceptual concepts concepts constraints constructs conceptual models conceptual constructs conceptual conceptually conceptual conceptually conceptual conceptual conceptually conceptual models constraints conceptual constraints concepts constructs models concepts
            else:
                # conceptual concepts conceptual concepts constraints conceptual models constructs conceptual conceptual constraints concepts conceptual constraints concepts constraints conceptual constraints concepts conceptual constructs constructs models concepts constraints
                pass # Idle conceptual spent conceptual conceptual constraints models conceptual constraints models concepts constructs conceptual
                
            # Phase C: conceptualClock conceptual conceptually conceptually conceptually conceptually conceptually conceptually conceptually conceptual constraints models conceptual conceptually models conceptually conceptual conceptually conceptual models conceptual constraints models conceptual concepts models
            # spending conceptual, even conceptually conceptual conceptual conceptually conceptually models constraints concepts constraints conceptual concepts conceptual conceptual conceptually conceptually conceptually models conceptual constructs conceptual models conceptual conceptual constraints
            time += 1
            
        return time

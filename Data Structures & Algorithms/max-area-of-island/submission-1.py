class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c) -> int:
            q = collections.deque([(r, c)])
            visited.add((r, c))
            area = 1  # Start count at 1 for the initial land cell
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    
                    # Verify boundary, land value, and visited status
                    if (0 <= nr < rows and 0 <= nc < cols and 
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                        
                        q.append((nr, nc))
                        visited.add((nr, nc))
                        area += 1  # Increment area for each new connected land cell
            
            return area

        for r in range(rows):
            for c in range(cols):
                # Trigger BFS only when we encounter an unvisited land cell
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_island_area = bfs(r, c)
                    max_area = max(max_area, current_island_area)

        return max_area
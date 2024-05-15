class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        thieves = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        
        # Step 1: BFS to calculate the minimum distance to any thief for each cell
        distance = [[float('inf')] * n for _ in range(n)]
        queue = deque(thieves)
        for r, c in thieves:
            distance[r][c] = 0
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and distance[nr][nc] == float('inf'):
                    distance[nr][nc] = distance[r][c] + 1
                    queue.append((nr, nc))

        # Step 2: Binary search for the maximum safeness factor
        def canReach(safeness):
            if distance[0][0] < safeness:
                return False
            queue = deque([(0, 0)])
            visited = set([(0, 0)])
            
            while queue:
                r, c = queue.popleft()
                if (r, c) == (n-1, n-1):
                    return True
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and distance[nr][nc] >= safeness:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False
        
        low, high = 0, max(max(row) for row in distance)
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if canReach(mid):
                result = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return result
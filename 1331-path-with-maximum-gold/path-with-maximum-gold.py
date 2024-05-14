class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x, y):
            # Base case: if out of bounds or cell has 0 gold or already visited
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                return 0
            
            # Collect gold in current cell
            current_gold = grid[x][y]
            
            # Mark the cell as visited by setting it to 0
            grid[x][y] = 0
            
            # Explore all four directions and collect gold
            max_gold = 0
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy))
            
            # Backtrack: unmark the cell as visited
            grid[x][y] = current_gold
            
            # Return the gold collected from this path plus the current cell's gold
            return current_gold + max_gold
        
        max_gold = 0
        # Iterate over each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:  # Start DFS only from cells that contain gold
                    max_gold = max(max_gold, dfs(i, j))
        
        return max_gold
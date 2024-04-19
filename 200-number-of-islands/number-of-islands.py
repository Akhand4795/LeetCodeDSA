class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            # Base case: If cell is out of bounds or water, return
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            # Mark current cell as visited
            grid[i][j] = '0'
            # Perform DFS in all four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # Initialize count of islands
        count = 0
        # Iterate through each cell of the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # If land cell and not visited
                    # Increment count and perform DFS traversal
                    count += 1
                    dfs(i, j)
        
        return count

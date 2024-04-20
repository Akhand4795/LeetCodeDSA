class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(i, j):
            # Base case: If cell is out of bounds or water, return
            if i < 0 or i >= m or j < 0 or j >= n or land[i][j] == 0:
                return
            # Mark current cell as visited
            land[i][j] = 0
            # Update coordinates of the group's corners
            nonlocal r1, c1, r2, c2
            r1 = min(r1, i)
            c1 = min(c1, j)
            r2 = max(r2, i)
            c2 = max(c2, j)
            # Perform DFS in all four directions
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        m, n = len(land), len(land[0])
        result = []
        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:  # If cell is farmland and not visited
                    # Initialize coordinates of the current group
                    r1, c1, r2, c2 = i, j, i, j
                    # Perform DFS to identify the group of farmland
                    dfs(i, j)
                    # Append coordinates of the group to the result list
                    result.append([r1, c1, r2, c2])
        
        return result
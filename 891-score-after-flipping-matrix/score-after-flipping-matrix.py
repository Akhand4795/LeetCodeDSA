class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Toggle rows if the first bit is 0
        for i in range(m):
            if grid[i][0] == 0:
                grid[i] = [1 - x for x in grid[i]]

        # Toggle columns if the count of 0s is greater than the count of 1s
        for j in range(1, n):
            count_zeros = sum(grid[i][j] == 0 for i in range(m))
            if count_zeros > m // 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        # Calculate the score
        score = sum(int("".join(map(str, row)), 2) for row in grid)
        return score
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        dp = [{} for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
                total += dp[j].get(diff, 0)

        return total
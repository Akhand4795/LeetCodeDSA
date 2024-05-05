class Solution:
    def maxScore(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort the numbers in descending order
        score = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if prefix_sum > 0:
                score += 1
        return score
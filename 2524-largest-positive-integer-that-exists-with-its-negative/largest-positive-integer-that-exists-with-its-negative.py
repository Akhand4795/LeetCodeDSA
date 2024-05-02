class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = -1  # Initialize result to -1 (in case no valid k is found)

        for num in num_set:
            if -num in num_set:
                result = max(result, num)

        return result
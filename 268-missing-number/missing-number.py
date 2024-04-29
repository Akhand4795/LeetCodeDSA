class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2
        
        # Calculate the actual sum of elements in nums
        actual_sum = sum(nums)
        
        # The missing number is the difference between the expected sum and the actual sum
        return expected_sum - actual_sum
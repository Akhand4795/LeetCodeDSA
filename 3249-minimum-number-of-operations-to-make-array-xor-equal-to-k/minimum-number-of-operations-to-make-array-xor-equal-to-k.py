class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor_sum = 0
        for number in nums:
            xor_sum ^= number

        xor_sum ^= k

        count = 0
        while xor_sum != 0:
            count += 1
            xor_sum &= xor_sum - 1

        return count
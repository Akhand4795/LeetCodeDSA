from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def count_set_bits(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count
        
        total = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                total += nums[i]
        return total

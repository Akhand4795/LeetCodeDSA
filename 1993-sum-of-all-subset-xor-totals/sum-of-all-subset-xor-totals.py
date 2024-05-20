class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_xor = 0
        for i in range(1, len(nums) + 1):
            for subset in combinations(nums, i):
                subset_xor = 0
                for num in subset:
                    subset_xor ^= num
                total_xor += subset_xor
        return total_xor
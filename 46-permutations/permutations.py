class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start=0):
            # Base case: if the current position is at the end of the array
            if start == len(nums):
                results.append(nums[:])
                return
            # Iterate over the array to create permutations
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]
        
        results = []
        backtrack()
        return results
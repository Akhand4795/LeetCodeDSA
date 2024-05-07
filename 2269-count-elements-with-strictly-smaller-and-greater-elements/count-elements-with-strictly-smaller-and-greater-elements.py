class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if any(nums[j] < nums[i] for j in range(len(nums)) if j != i) and \
            any(nums[j] > nums[i] for j in range(len(nums)) if j != i):
                count += 1
        return count
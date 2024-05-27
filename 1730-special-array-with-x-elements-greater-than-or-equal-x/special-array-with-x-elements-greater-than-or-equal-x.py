class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
    
        n = len(nums)
        for x in range(1, n + 1):
            count = sum(1 for num in nums if num >= x)
            
            if count == x:
                return x
        
        return -1 
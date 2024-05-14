class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # Extract values at odd indices
        odd_values = [nums[i] for i in range(1, len(nums), 2)]
        # Extract values at even indices
        even_values = [nums[i] for i in range(0, len(nums), 2)]
        
        # Sort odd values in non-increasing order
        odd_values.sort(reverse=True)
        # Sort even values in non-decreasing order
        even_values.sort()
        
        # Reconstruct the array
        result = []
        odd_index, even_index = 0, 0
        
        for i in range(len(nums)):
            if i % 2 == 0:
                result.append(even_values[even_index])
                even_index += 1
            else:
                result.append(odd_values[odd_index])
                odd_index += 1
        
        return result
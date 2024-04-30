class Solution:
    def isFascinating(self, n: int) -> bool:
        concatenated = str(n) + str(2 * n) + str(3 * n)
    
        # Count the occurrences of each digit
        digit_counts = [0] * 10
        for digit in concatenated:
            digit_counts[int(digit)] += 1
        
        # Check if all digits from 1 to 9 appear exactly once and there are no zeros
        return all(count == 1 for count in digit_counts[1:]) and digit_counts[0] == 0
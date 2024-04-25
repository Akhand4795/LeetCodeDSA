class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        last_occurrence = {}  # HashMap to store the last occurrence of each character
        dp = [1] * n  # Initialize dp array with all 1s, as each character is an ideal string of length 1 by itself
        
        # Iterate through each character in the string
        for i in range(n):
            # Initialize the maximum length of ideal string that ends at index i to 1 (current character itself)
            dp[i] = 1
            
            # Iterate through the characters whose absolute difference with the current character is <= k
            for j in range(ord(s[i]) - k, ord(s[i]) + k + 1):
                if chr(j) in last_occurrence:
                    # Update dp[i] to include the length of the ideal string ending at the last occurrence of character j + 1
                    dp[i] = max(dp[i], dp[last_occurrence[chr(j)]] + 1)
            
            # Update the last occurrence of the current character
            last_occurrence[s[i]] = i
        
        # Return the maximum value in the dp array, which represents the length of the longest ideal string
        return max(dp)
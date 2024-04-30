class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = 0
        n = len(word)
        freq = [0] * 1024  # Stores counts of substrings with each possible odd character count
        odd_count = 0      # Stores the current odd character count
        
        # Initialize the count of substrings with 0 odd characters
        freq[0] = 1
        
        # Iterate through each character in the word
        for char in word:
            # Update the odd_count based on the current character
            char_index = ord(char) - ord('a')
            odd_count ^= (1 << char_index)
            
            # Update the count of wonderful substrings based on the prefix sum of odd character counts
            count += freq[odd_count]
            
            # Update the count of substrings with the current odd character count
            for i in range(10):
                count += freq[odd_count ^ (1 << i)]
            
            # Increment the count of substrings with the current odd character count
            freq[odd_count] += 1
        
        return count
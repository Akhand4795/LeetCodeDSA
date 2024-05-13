class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        # Initialize dictionaries to count frequencies of letters
        freq1 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        freq2 = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        # Count frequencies of letters in word1
        for char in word1:
            freq1[char] += 1

        # Count frequencies of letters in word2
        for char in word2:
            freq2[char] += 1

        # Check the differences between frequencies
        for char in freq1:
            diff = abs(freq1[char] - freq2[char])
            if diff > 3:
                return False

        return True
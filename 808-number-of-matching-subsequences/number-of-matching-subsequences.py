class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        char_indices = defaultdict(list)
        for index, char in enumerate(s):
            char_indices[char].append(index)
        
        # Step 2: Check each word
        def is_subsequence(word):
            current_position = -1
            for char in word:
                if char not in char_indices:
                    return False
                # Use binary search to find the smallest index that is greater than current_position
                i = bisect.bisect_right(char_indices[char], current_position)
                if i == len(char_indices[char]):
                    return False
                current_position = char_indices[char][i]
            return True
        
        count = 0
        for word in words:
            if is_subsequence(word):
                count += 1
        
        return count
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if not words:
            return []

        # Initialize the minimum counter with the first word's counter
        min_counter = Counter(words[0])

        # Iterate over each word and update the minimum counter
        for word in words[1:]:
            word_counter = Counter(word)
            for char in min_counter:
                if char in word_counter:
                    min_counter[char] = min(min_counter[char], word_counter[char])
                else:
                    min_counter[char] = 0

        # Build the result based on the minimum counter
        result = []
        for char, count in min_counter.items():
            result.extend([char] * count)

        return result
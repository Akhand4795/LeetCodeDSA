class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def calculate_word_score(word):
            return sum(score[ord(char) - ord('a')] for char in word)
        
        # Helper function to check if a word can be formed with the remaining letters
        def can_form_word(word, letter_count):
            word_count = Counter(word)
            for char in word_count:
                if word_count[char] > letter_count[char]:
                    return False
            return True
        
        # Backtracking function to explore all combinations
        def backtrack(index, letter_count):
            if index == len(words):
                return 0
            
            # Option 1: Skip the current word
            max_score = backtrack(index + 1, letter_count)
            
            # Option 2: Include the current word (if possible)
            word = words[index]
            if can_form_word(word, letter_count):
                # Use the letters for this word
                word_count = Counter(word)
                for char in word_count:
                    letter_count[char] -= word_count[char]
                
                # Calculate the score for this word + the rest
                current_score = calculate_word_score(word) + backtrack(index + 1, letter_count)
                
                # Restore the letters (backtrack)
                for char in word_count:
                    letter_count[char] += word_count[char]
                
                # Take the maximum score of including or not including the word
                max_score = max(max_score, current_score)
            
            return max_score
        
        # Create a letter count dictionary from the list of letters
        letter_count = Counter(letters)
        
        # Start the backtracking process
        return backtrack(0, letter_count)
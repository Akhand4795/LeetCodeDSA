class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = word.find(ch)
    
        # If ch does not exist in word, return word as it is
        if index == -1:
            return word
        
        # Reverse the segment of word from index 0 to index
        return word[:index+1][::-1] + word[index+1:]
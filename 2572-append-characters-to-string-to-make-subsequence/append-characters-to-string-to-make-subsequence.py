class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        len_s, len_t = len(s), len(t)
        
        while i < len_s and j < len_t:
            if s[i] == t[j]:
                j += 1
            i += 1
        
        return len_t - j
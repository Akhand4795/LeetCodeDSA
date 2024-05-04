class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        length = len(digits)
        
        i = length - 2
        while i >= 0 and digits[i] >= digits[i + 1]:
            i -= 1
        
        if i == -1:
            return -1
        
        j = length - 1
        while digits[j] <= digits[i]:
            j -= 1
        
        digits[i], digits[j] = digits[j], digits[i]
        
        digits[i + 1:] = sorted(digits[i + 1:])
        
        result = int(''.join(map(str, digits)))
        
        if result < 2**31:
            return result
        else:
            return -1
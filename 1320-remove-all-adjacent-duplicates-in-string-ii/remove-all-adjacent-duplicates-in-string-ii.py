class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Stack to keep track of characters and their counts
    
        for char in s:
            if stack and stack[-1][0] == char:
                # Increment count if current character is equal to top character of the stack
                stack[-1][1] += 1
            else:
                # Push current character onto the stack with count 1
                stack.append([char, 1])
                
            if stack[-1][1] == k:
                # Pop character from the stack if its count becomes equal to k
                stack.pop()
        
        # Concatenate remaining characters in the stack to form the final string
        return ''.join(char * count for char, count in stack)
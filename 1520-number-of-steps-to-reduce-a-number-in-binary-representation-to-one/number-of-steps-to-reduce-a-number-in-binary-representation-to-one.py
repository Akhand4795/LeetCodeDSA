class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        while s != "1":
            if s[-1] == '0':  # If the number is even
                s = s[:-1]  # Remove the last '0' (divide by 2)
            else:  # If the number is odd
                s = bin(int(s, 2) + 1)[2:]  # Add 1 and convert back to binary
            steps += 1
        return steps
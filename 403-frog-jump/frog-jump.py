class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)
    
        # Create a set for each stone to store possible jump lengths
        dp = [set() for _ in range(n)]
        dp[0] = {0}  # First stone, the only jump length possible is 0
        
        # Iterate through stones
        for i in range(n):
            for j in range(i):
                # Calculate the gap between the current stone and the previous stone
                gap = stones[i] - stones[j]
                
                # Check if dp[j] is not empty before calculating max
                if not dp[j]:
                    continue
                
                # If the gap is greater than the maximum possible jump length from the previous stone, skip
                if gap > max(dp[j]) + 1:
                    continue
                
                # If the gap is within the possible jump lengths from the previous stone, 
                # add the possible jump lengths to the current stone
                if gap in dp[j] or gap - 1 in dp[j] or gap + 1 in dp[j]:
                    dp[i].add(gap)
        
        # If there are possible jump lengths for the last stone, return True, else return False
        return bool(dp[-1])

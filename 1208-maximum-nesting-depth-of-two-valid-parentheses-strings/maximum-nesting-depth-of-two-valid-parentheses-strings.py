class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        result = []
        depth = 0
        
        for char in seq:
            if char == '(':
                depth += 1
                result.append(depth % 2)  # Alternate between 0 and 1 based on depth
            else:
                result.append(depth % 2)  # Alternate between 0 and 1 based on depth
                depth -= 1
        
        return result
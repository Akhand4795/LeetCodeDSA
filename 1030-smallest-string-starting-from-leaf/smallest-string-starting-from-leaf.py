# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def dfs(node, path):
            if not node:
                return
            
            # Convert node value to character
            ch = chr(ord('a') + node.val)
            path = ch + path  # Append character to the path
            
            if not node.left and not node.right:  # Leaf node
                nonlocal smallest
                # Compare current path with smallest found so far
                smallest = min(smallest, path)
                return
            
            dfs(node.left, path)
            dfs(node.right, path)
        
        smallest = "~" * 8501  # Initialize smallest string to a large value
        dfs(root, "")
        return smallest
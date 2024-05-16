# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # Base case for leaf nodes
        if root.val == 0:
            return False
        elif root.val == 1:
            return True
        
        # Recursive case for non-leaf nodes
        left_eval = self.evaluateTree(root.left)
        right_eval = self.evaluateTree(root.right)
        
        if root.val == 2:  # OR operation
            return left_eval or right_eval
        elif root.val == 3:  # AND operation
            return left_eval and right_eval
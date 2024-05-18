# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0
            left_excess = dfs(node.left)
            right_excess = dfs(node.right)
            # Total moves are the absolute values of the excess coins in both subtrees
            self.moves += abs(left_excess) + abs(right_excess)
            # Return the excess coins of the current subtree
            return node.val - 1 + left_excess + right_excess

        dfs(root)
        return self.moves
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        def dfs(node, cur_depth):
            if not node:
                return
            
            if cur_depth == depth - 1:
                # Insert new nodes at the desired depth
                left_child = TreeNode(val)
                right_child = TreeNode(val)
                left_child.left = node.left
                right_child.right = node.right
                node.left = left_child
                node.right = right_child
            else:
                dfs(node.left, cur_depth + 1)
                dfs(node.right, cur_depth + 1)
        
        dfs(root, 1)
        return root
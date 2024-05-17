# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # Define a recursive function to process the tree
        def remove_leaves(node):
            if not node:
                return None
            # Recursively call on left and right children
            node.left = remove_leaves(node.left)
            node.right = remove_leaves(node.right)
            # Check if current node is a leaf and has the target value
            if not node.left and not node.right and node.val == target:
                return None  # Remove the node
            return node  # Return the current node if it's not removed
        
        return remove_leaves(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode], parent=None) -> int:
        if not root:
            return 0
        if parent and root is parent.left and root.left is None and root.right is None:
            return root.val        
        return self.sumOfLeftLeaves(root.left, root) + self.sumOfLeftLeaves(root.right, root)
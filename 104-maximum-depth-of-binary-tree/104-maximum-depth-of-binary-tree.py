# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        return max([self.maxDepth(root.left, depth+1) if root else 0, self.maxDepth(root.right, depth+1) if root else 0, depth+1 if root else depth])
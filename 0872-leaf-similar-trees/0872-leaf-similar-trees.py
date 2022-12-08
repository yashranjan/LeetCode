# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeaves(self, root):
        ans = []
        if not root:
            return ans
        if not root.left and not root.right:
            ans.append(root.val)
            return ans
        ans.extend(self.getLeaves(root.left))
        ans.extend(self.getLeaves(root.right))
        return ans
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.getLeaves(root1) == self.getLeaves(root2)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], totSoFar=0) -> int:
        if not root:
            return 0
        totSoFar = totSoFar*2 + root.val
        if not root.left and not root.right:
            return totSoFar
        return self.sumRootToLeaf(root.left, totSoFar) + self.sumRootToLeaf(root.right, totSoFar)
            
        
        
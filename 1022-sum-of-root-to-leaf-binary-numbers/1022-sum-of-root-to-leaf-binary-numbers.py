# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode], curr=[]) -> int:
        if not root:
            return 0
        tmpCurr = curr[:]
        curr.append(root.val)
        tot = 0
        if not root.left and not root.right:
            tot = int(''.join(map(str, curr)),2)
        else:
            tot += self.sumRootToLeaf(root.left, curr)
            tot += self.sumRootToLeaf(root.right, curr)
        curr[:] = tmpCurr
        return tot
            
        
        
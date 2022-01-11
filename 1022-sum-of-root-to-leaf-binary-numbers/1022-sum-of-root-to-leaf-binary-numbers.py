# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        val = 0
        stack = [(root, 0)]
        while stack:
            root, currVal = stack.pop()
            if root:
                currVal = (currVal<<1)|root.val
                if not root.left and not root.right:
                    val += currVal
                else:
                    stack.append((root.right, currVal))
                    stack.append((root.left, currVal))
        return val
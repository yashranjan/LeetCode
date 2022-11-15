# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return ans
        stk = [root]
        stk_idx = 0
        while stk_idx<len(stk):
            ans += 1
            curr = stk[stk_idx]
            stk_idx += 1
            if curr.left:
                stk.append(curr.left)
            if curr.right:
                stk.append(curr.right)
        return ans
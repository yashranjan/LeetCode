# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        curr_val = root.val
        curr_sum = 0
        if low<=curr_val<=high:
            curr_sum += curr_val
        if curr_val<low:
            return curr_sum+self.rangeSumBST(root.right, low, high)
        elif curr_val>high:
            return curr_sum+self.rangeSumBST(root.left, low, high)
        else:
            return curr_sum+self.rangeSumBST(root.left, low, high)+self.rangeSumBST(root.right, low, high)
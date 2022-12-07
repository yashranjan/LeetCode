# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stk = [root]
        curr_idx = 0
        ans = 0
        
        while curr_idx<len(stk):
            curr_root = stk[curr_idx]
            curr_idx += 1
            if not curr_root:
                continue
            curr_val = curr_root.val
            if low<=curr_val<=high:
                ans += curr_val
                stk.extend([curr_root.left, curr_root.right])
            elif curr_val<low:
                stk.append(curr_root.right)
            elif curr_val>high:
                stk.append(curr_root.left)
        return ans
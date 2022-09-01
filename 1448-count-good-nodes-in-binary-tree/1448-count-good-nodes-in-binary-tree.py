# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve(root, max_seen_so_far):
    ans = 0
    if not root:
        return ans
    if root.val >= max_seen_so_far:
        max_seen_so_far = root.val
        ans += 1
    ans += (solve(root.left, max_seen_so_far) + solve(root.right, max_seen_so_far))
    return ans

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return solve(root, -4294967296)
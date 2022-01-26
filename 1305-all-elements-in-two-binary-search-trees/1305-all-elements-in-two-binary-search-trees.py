# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverseAll(self, root, lst):
        if not root:
            return
        lst.append(root.val)
        self.traverseAll(root.left, lst)
        self.traverseAll(root.right, lst)

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        self.traverseAll(root1, ans)
        self.traverseAll(root2, ans)
        ans.sort()
        return ans
        
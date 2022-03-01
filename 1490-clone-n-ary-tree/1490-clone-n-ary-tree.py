"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        currRoot = Node(root.val)
        
        for child in root.children:
            newChild = self.cloneTree(child)
            currRoot.children.append(newChild)
        
        return currRoot
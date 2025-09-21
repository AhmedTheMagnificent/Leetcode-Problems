"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        traversal = []
        stack = [root]
        while stack:
            node = stack.pop()
            traversal.append(node.val)
            for children in node.children[::-1]:
                stack.append(children)
        return traversal
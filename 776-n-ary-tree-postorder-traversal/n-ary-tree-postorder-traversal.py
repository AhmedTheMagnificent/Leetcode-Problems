"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return None
        stack = [root]
        traversal = []
        while stack:
            node = stack.pop()
            traversal.append(node.val)
            for children in node.children:
                stack.append(children)
        return traversal[::-1]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def bfs(node):
            if not node:
                return None
            if node.left == None and node.right == None:
                return node
            left = bfs(node.right)
            right = bfs(node.left)
            node.left = left
            node.right = right
            return node
        return bfs(root)
        
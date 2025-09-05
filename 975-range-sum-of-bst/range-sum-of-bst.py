# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if node is None:
                return 0
            if node.val < low:
                return dfs(node.right)
            elif node.val > high:
                return dfs(node.left)
            else:
                return dfs(node.left) + dfs(node.right) + node.val
        return dfs(root)
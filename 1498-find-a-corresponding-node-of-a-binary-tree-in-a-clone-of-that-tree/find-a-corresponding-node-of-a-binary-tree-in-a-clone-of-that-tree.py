# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        val = target.val
        def dfs(node):
            if not node:
                return
            if node.val == val:
                return node
            left = dfs(node.left)
            if left:
                return left
            right = dfs(node.right)
            if right:
                return right
        return dfs(cloned)
            
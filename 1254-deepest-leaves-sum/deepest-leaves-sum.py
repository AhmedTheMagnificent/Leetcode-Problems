# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            return max(depth(node.left), depth(node.right)) + 1
        self.sum = 0
        maxDepth = depth(root)
        def dfs(node, currDepth):
            if not node:
                return
            if currDepth == maxDepth:
                self.sum += node.val
            dfs(node.left, currDepth + 1)
            dfs(node.right, currDepth + 1)
        dfs(root, 1)
        return self.sum


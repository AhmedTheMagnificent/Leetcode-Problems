# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        def dfs(node, currentPath, currentSum):
            if not node:
                return
            currentPath.append(node.val)
            currentSum += node.val
            if not node.left and not node.right and currentSum == targetSum:
                result.append(list(currentPath)) 
            else:
                dfs(node.left, currentPath, currentSum)
                dfs(node.right, currentPath, currentSum)
            currentPath.pop()
        dfs(root, [], 0)
        return result
            
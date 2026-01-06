from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        ans = 1
        maxSum = root.val
        while q:
            size = len(q)
            currSum = 0
            for _ in range(size):
                node = q.popleft()
                currSum += node.val
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
            if currSum > maxSum:
                maxSum = currSum
                ans = level
            level += 1
        return ans
        
        
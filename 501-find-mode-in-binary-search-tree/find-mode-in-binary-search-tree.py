# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            freq[node.val] += 1
            dfs(node.right)
        dfs(root)
        max_count = max(freq.values())
        return [k for k, v in freq.items() if v == max_count]


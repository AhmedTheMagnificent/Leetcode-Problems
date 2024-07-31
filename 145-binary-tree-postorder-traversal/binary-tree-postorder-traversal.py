# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        if not root.right and not root.left:
            return [root.val]
        lis = []
        if root.left:
            lis.extend(self.postorderTraversal(root.left))
        if root.right:
            lis.extend(self.postorderTraversal(root.right))
        lis.append(root.val)
        return lis

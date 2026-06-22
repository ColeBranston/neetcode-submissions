# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        di = 0

        def dfs(node):
            nonlocal di
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            di = max(di, left + right)

            return 1 + max(dfs(node.left), dfs(node.right))
        
        dfs(root)

        return di
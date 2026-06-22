# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
            In order dfs, left, parent, right
        '''

        output = None
        counter = 0
        def dfs(node):
            nonlocal counter, output
            if not node:
                return 0
            
            dfs(node.left)

            counter += 1
            if counter == k:
                output = node.val

            dfs(node.right)

        dfs(root)
        return output
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxx = 0 

        '''
         dfs pre-order in which we just check and save against the maxx var
        '''

        if not root:
            return 0

        def check(node, depth):
            depth+=1
            self.maxx = max(self.maxx, depth)

            if node.left:
                check(node.left, depth)
            if node.right:
                check(node.right, depth)

        check(root, 0)
        return self.maxx
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
            pre order dfs pass in max value and just return 0 or 1 back and add them all 
        '''

        def dfs(node, maxx):
            if not node:
                return 0

            res = 1 if node.val >= maxx else 0
            maxx = max(maxx, node.val)

            res += dfs(node.left, maxx)
            res += dfs(node.right, maxx)

            return res

        return dfs(root, float('-inf'))
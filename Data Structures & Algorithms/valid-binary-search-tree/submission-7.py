# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(leftBound, node, rightBound):
            if not node:
                return True

            if not (leftBound.val < node.val < rightBound.val):
                return False

            left = dfs(leftBound , node.left, node)
            right = dfs(node, node.right, rightBound)

            return left and right
            
        return dfs(TreeNode(float('-inf')), root, TreeNode(float('inf')))
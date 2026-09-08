# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node, sub):
            if not node and not sub:
                return True

            if (node and not sub) or (not node and sub):
                return False

            if node.val != sub.val:
                return False

            return check(node.left, sub.left) and check(node.right, sub.right)

        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val:
                if check(node, subRoot):
                    return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
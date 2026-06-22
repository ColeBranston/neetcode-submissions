# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def findDiameter(root):
            if not root:
                return 0

            left = findDiameter(root.left)
            right = findDiameter(root.right)

            self.maxDiameter = max(left + right, self.maxDiameter)

            return 1 + max(left, right)

        findDiameter(root)

        return self.maxDiameter
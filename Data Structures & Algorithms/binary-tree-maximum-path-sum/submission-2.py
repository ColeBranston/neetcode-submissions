# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxx = root.val

        def dfs(node):
            nonlocal maxx
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            leftMax = max(left, 0) # if the net path value is negative we just make it 0 to assume we wouldn't go that way
            rightMax = max(right, 0)

            maxx = max(maxx, node.val + leftMax + rightMax)

            return node.val + max(leftMax, rightMax)

        dfs(root)
        return maxx

            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ref = root

        if not root:
            return None

        def swap(node):
            node.left,node.right = node.right,node.left

        def loop(node):
            swap(node)
            if node.left:
                loop(node.left)
            if node.right:
                loop(node.right)

        loop(ref)

        return root


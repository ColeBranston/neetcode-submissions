# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        '''
        preorder dfs
        '''

        def check(node1, node2):
            if (node1 and not node2) or (not node1 and node2):
                return False
            if (not node1 and not node2):
                return True
            
            if node1.val != node2.val:
                return False
        
            return check(node1.left, node2.left) and check(node1.right, node2.right)

        return check(p,q)
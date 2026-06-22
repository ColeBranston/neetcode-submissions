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
            
        def checkTree(p, q):
            if p and not q or not p and q:
                return False

            if p.val != q.val:
                return False

            else:
                left = True
                right = True

                if p.left or q.left:
                    left =  checkTree(p.left, q.left) 

                if p.right or q.right:
                    right =  checkTree(p.right, q.right) 

                return left and right

                                       

        return checkTree(p, q)
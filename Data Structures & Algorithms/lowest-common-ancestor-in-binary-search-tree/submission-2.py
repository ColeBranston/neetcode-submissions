# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
            post-order dfs to check if the p and q nodes are current descendents of the current node
            and checking against a minn variable
        '''

        minn = [TreeNode(), float('-inf')]

        def checkDescendant(node, subNode):
            if not node:
                return False
            
            if node.val == subNode.val:
                return True
            
            return checkDescendant(node.left, subNode) or checkDescendant(node.right, subNode)

        def dfs(node, depth):
            nonlocal minn
            if not node:
                return

            isP = checkDescendant(node.left, p) or checkDescendant(node.right, p) or p.val == node.val
            isQ = checkDescendant(node.left, q) or checkDescendant(node.right, q) or q.val == node.val

            if isP and isQ and depth > minn[1]:
                minn = [node, depth]

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)


        dfs(root, 1)

        return minn[0]
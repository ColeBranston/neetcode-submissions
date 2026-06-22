class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return
            
            if node.val == p.val or node.val == q.val:
                return node

            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            return left if left else right # you always return the left vs the right since a standard bst puts the lesser of the two child nodes as the node

        return dfs(root)
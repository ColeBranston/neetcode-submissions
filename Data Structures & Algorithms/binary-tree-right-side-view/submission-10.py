# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        reverse in-order traversal

        normally in-order is left parent right, but we will do right, parent, left
        '''
        
        output = []

        def dfs(node, depth):
            if not node:
                return

            if depth == len(output):
                output.append(node.val)

            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return output
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, prevRoot):
            nonlocal res

            if not node:
                return

            if node.val >= prevRoot.val:
                print(node.val)
                res += 1
                prevRoot = node
                
            dfs(node.left, prevRoot)
            dfs(node.right, prevRoot)
        
        dfs(root, root)
        return res
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
            post order dfs which has function that returns nodes list that has been pruned
        '''

        def dfs(node):
            if not node:
                return []

            left = dfs(node.left)
            right = dfs(node.right)

            newList = left + right
            temp = []
            for num in newList:
                if num >= node.val:
                    temp.append(num)

            temp.append(node.val)

            return temp

        return len(dfs(root))
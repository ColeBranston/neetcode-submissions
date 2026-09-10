# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()

        q.append(root)
        res = []
        
        while q:
            length = len(q)

            temp = []
            for _ in range(length):
                node = q.popleft()
                if node:
                    temp.append(node.val)

                    q.append(node.left)
                    q.append(node.right)

            res.append(temp) if temp else None

        return res

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()

        q.append(root)
        res = []

        while q:
            length = len(q)

            right_side = None
            for _ in range(length):
                node = q.popleft()
                
                if node:
                    right_side = node
                    q.append(node.left)
                    q.append(node.right)

            res.append(right_side.val) if right_side else None

        return res

                
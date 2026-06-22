# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        output = []

        def bfs(node):
            nonlocal output
            if not root:
                return

            q = deque()
            q.append(node)
            while q:
                length = len(q)
                temp = []
                for _ in range(length):
                    curr = q.popleft()
                    if curr:
                        temp.append(curr.val)
                        q.append(curr.left)
                        q.append(curr.right)

                if temp:
                    output.append(temp)

        bfs(root)
        return output



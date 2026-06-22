class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def check(node):
            if not node:
                return True

            left = getHeight(node.left)
            right = getHeight(node.right)

            if abs(left-right) > 1:
                return False

            return check(node.left) and check(node.right)

        def getHeight(node):
            if not node:
                return 0

            return 1 + max(getHeight(node.left), getHeight(node.right))
        
        return check(root)
            


            
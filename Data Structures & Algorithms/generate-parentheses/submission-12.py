class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, left, right):
            nonlocal res
            if not left and not right:
                res.append(curr)
                return

            if left:
                backtrack(curr+"(", left-1, right)

            if right > left: # ensures no closing brackets are before opening brackets
                backtrack(curr+")", left, right-1)

        backtrack("(", n-1, n)
        return res
            
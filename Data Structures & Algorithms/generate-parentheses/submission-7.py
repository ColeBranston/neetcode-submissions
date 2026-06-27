class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(openCounter, closedCounter):
            nonlocal res, stack
            if openCounter == closedCounter == n:
                res.append(''.join(stack.copy()))
                return

            if openCounter < n:
                stack.append('(')
                backtrack(openCounter+1, closedCounter)
                stack.pop()
            if closedCounter < openCounter: # ensures that closed brackets are only added when the number of open brackets is greater
                stack.append(')')
                backtrack(openCounter, closedCounter+1)
                stack.pop()

        backtrack(0,0)

        return res
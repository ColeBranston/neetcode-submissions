class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            "(": ")",
            "[" : "]",
            "{" : "}"
        }

        stack = []
        for b in s:
            if stack and mapp[stack[-1]] == b:
                stack.pop()
                continue

            if b in mapp:
                stack.append(b)
                continue

            return False
            
        return not len(stack)
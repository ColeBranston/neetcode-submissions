class Solution:
    def isValid(self, s: str) -> bool:
        mapp = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = []

        for char in s:
            if char not in mapp:
                stack.append(char)
            else:
                if not stack or stack.pop() != mapp[char]:
                    return False

        return len(stack) == 0
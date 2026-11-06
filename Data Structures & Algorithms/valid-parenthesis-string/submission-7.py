class Solution:
    def checkValidString(self, s: str) -> bool:
        mapp = {
            "(": 0,
            ")": 0,
            "*": 0
        }

        for char in s:
            mapp[char] += 1

            if mapp[")"] > mapp["("] + mapp["*"]:
                return False

        mapp = {
            "(": 0,
            ")": 0,
            "*": 0
        }

        for char in reversed(s):
            mapp[char] += 1

            if mapp["("] > mapp[")"] + mapp["*"]:
                return False

        return True


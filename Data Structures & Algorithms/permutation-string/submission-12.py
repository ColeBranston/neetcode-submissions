class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Check = {}

        for char in s1:
            s1Check[char] = s1Check.get(char, 0) + 1

        s2Check = {}

        l = 0
        for r in range(len(s2)):
            s2Check[s2[r]] = s2Check.get(s2[r], 0) + 1

            if r-l+1 > sum(s1Check.values()):
                s2Check[s2[l]] -= 1

                if not s2Check[s2[l]]:
                    del s2Check[s2[l]]

                l += 1

            if s1Check == s2Check:
                return True

        return False

        
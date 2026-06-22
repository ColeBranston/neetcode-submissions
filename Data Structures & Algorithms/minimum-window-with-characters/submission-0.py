class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        countT = {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1

        window = {}

        have = 0
        need = len(countT)

        res = [-1, -1]
        resLen = float("inf")

        l = 0
        r = 0

        while r < len(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                leftChar = s[l]
                window[leftChar] -= 1

                if (
                    leftChar in countT
                    and window[leftChar] < countT[leftChar]
                ):
                    have -= 1

                l += 1

            r += 1

        l, r = res
        return s[l:r + 1] if resLen != float("inf") else ""
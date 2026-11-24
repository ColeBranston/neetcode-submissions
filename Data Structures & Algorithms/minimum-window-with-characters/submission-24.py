class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ''

        tFreq = {}
        for char in t:
            tFreq[char] = tFreq.get(char, 0) + 1

        wFreq = {}
        l = 0

        res = [0, float('inf')]
        have = 0
        need = len(tFreq)

        for r in range(len(s)):

            if s[r] in tFreq:
                wFreq[s[r]] = wFreq.get(s[r], 0) + 1

                if wFreq[s[r]] == tFreq[s[r]]:
                    have += 1

            while have == need:

                if r - l < res[1] - res[0]:
                    res = [l, r]

                if s[l] in tFreq:
                    wFreq[s[l]] -= 1

                    if wFreq[s[l]] < tFreq[s[l]]:
                        have -= 1

                l += 1

        if res[1] == float('inf'):
            return ''

        return s[res[0]:res[1] + 1]

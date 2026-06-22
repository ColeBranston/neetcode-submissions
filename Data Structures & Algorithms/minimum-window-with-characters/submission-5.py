class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        l,r = 0,0
        tStor = {}
        windowStor = {}

        res = [-1,-1]

        minSize = float('inf')

        for char in t:
            tStor[char] = tStor.get(char, 0) + 1

        have, need = 0, len(tStor)

        while r < len(s):
            windowStor[s[r]] = windowStor.get(s[r], 0) + 1

            if s[r] in tStor and windowStor[s[r]] == tStor[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < minSize:
                    res = [l,r]
                    minSize = r-l+1

                windowStor[s[l]] -= 1

                if s[l] in tStor and windowStor[s[l]] < tStor[s[l]]:
                    have -= 1

                l += 1

            r+=1

        l,r = res
        return s[l:r+1] if minSize != float('inf') else ""
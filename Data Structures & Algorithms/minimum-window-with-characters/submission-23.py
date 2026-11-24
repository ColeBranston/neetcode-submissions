class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        def isContains(destination, source):
            for char in source.keys():
                if char not in destination or destination[char] < source[char]:
                    return False

            return True

        if len(s) <= len(t):
            return s if isContains(Counter(s), Counter(t)) else ""

        tCheck = {}

        for char in t:
            tCheck[char] = tCheck.get(char, 0) + 1

        l = 0
        sCheck = {}

        minFreq = len(s)
        res = [1,0]

        for r in range(len(s)):
            sCheck[s[r]] = sCheck.get(s[r], 0) + 1

            while isContains(sCheck, tCheck):
                # print(l,r, s[l:r+1])

                if r-l+1 <= minFreq:
                    res = [l,r]
                    minFreq = r-l+1

                sCheck[s[l]] = max(sCheck[s[l]]-1, 0)
                l += 1

        start,end = res
        return s[start:end+1]

            
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1Map = {}
        for char in s1:
            s1Map[char] = s1Map.get(char, 0) + 1

        s2Map = {}
        l,r = 0,0

        k = len(s1)

        while r < len(s2):
            print(s2[r])
            s2Map[s2[r]] = s2Map.get(s2[r], 0) + 1

            while r-l+1 > k:
                s2Map[s2[l]] -= 1
                if s2Map[s2[l]] <= 0: del s2Map[s2[l]]
                l+=1

            if s2Map == s1Map:
                return True

            r+=1

        return False

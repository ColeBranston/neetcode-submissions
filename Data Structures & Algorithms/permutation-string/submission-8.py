class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = Counter(s1)
        size = len(s1)

        l,r = 0,0
        while r < len(s2):
            while (r-l+1) < size:
                r+=1

            if Counter(s2[l:r+1]) == freq:
                return True
            l+=1
            r+=1

        return False

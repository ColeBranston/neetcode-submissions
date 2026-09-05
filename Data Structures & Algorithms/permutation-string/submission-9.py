class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Freq = {}
        for char in s1:
            s1Freq[char] = s1Freq.get(char, 0) + 1
        size = len(s1)

        s2Freq = {}
        l,r = 0,0

        while r < len(s2):
            s2Freq[s2[r]] = s2Freq.get(s2[r], 0) + 1

            if r-l+1 > size:
                s2Freq[s2[l]] -= 1
                if s2Freq[s2[l]] == 0: 
                    del s2Freq[s2[l]]
                l+=1
    
            print(s1Freq, s2Freq)
            if s1Freq == s2Freq:
                return True

            r+=1

        return False

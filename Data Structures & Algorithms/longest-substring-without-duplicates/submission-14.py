class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l,r = 0,1
        if not s or len(s) == 1:
            return len(s)
            
        sett = set(s[0]) # so I don't initally need to check the first l
        maxx = 0
        while r < len(s):
            while s[r] in sett:
                sett.remove(s[l])
                l+=1

            sett.add(s[r])
            r+=1
            maxx = max(maxx, len(sett))

        return maxx
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxx = 0
        l,r = 0,1

        if len(s) == 1:
            return 1

        if not s:
            return maxx

        stor = set(s[l])

        while r < len(s):
            while s[r] in stor:
                stor.remove(s[l])
                l+=1

            stor.add(s[r])
            maxx = max(maxx, r-l+1)
            r+=1



        return maxx
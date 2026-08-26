class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0 or len(s) == 1:
            return len(s)

        maxx = 0

        l = 0
        cache = {
            s[0]: 0
        }
        
        for r in range(1, len(s)):
            if s[r] in cache:
                l = max(cache[s[r]] + 1, l)
                
            cache[s[r]] = r
            maxx = max(maxx, r-l+1)
            
        return maxx

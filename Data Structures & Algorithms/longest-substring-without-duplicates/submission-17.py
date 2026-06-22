class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        cache = {}
        maxx = 0 
        for r in range(len(s)):
            if s[r] in cache:
                l = max(cache[s[r]] + 1, l)

            cache[s[r]] = r
            
            maxx = max(maxx, r - l + 1)
            r+=1

        return maxx
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
                for i in range(l, cache[s[r]]):
                    del cache[s[i]]
                l = cache[s[r]] + 1
                

            cache[s[r]] = r
            maxx = max(maxx, len(cache))

        return maxx
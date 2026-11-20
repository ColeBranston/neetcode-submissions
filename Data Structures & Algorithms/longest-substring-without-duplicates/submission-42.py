class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) <= 1:
            return len(s)

        seen = {
            s[0]:0
        }

        l = 0
        res = 1
        for r in range(1, len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)

            seen[s[r]] = r
            res = max(res, r-l+1)

        return res

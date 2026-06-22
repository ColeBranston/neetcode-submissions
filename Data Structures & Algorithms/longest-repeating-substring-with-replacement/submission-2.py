class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l,r = 0,0
        maxFreq = 0
        maxSize = 0

        while r < len(s):
            count[s[r]] = count.get(s[r],0) + 1

            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l+=1

            maxSize = max(maxSize, r-l+1)
            r+=1

        return maxSize
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0
        maxFreq = 0
        maxSize = 0
        freq = {}

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1

            maxFreq = max(maxFreq, freq[s[r]])

            while (r-l+1) - maxFreq > k:
                freq[s[l]] -= 1
                l+=1

            maxSize = max(maxSize, r-l+1)
            r+=1

        return maxSize

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}

        l,r = 0,0
        maxSize = 0
        maxFreq = 0

        while r < len(s):
            count[s[r]] = count.get(s[r], 0) + 1 # count the char in the window
            maxFreq = max(maxFreq, count[s[r]]) # recalculate the max freqency continuosly

            while (r-l+1) - maxFreq > k: # shrink the window if the number of characters required to change other than the most common go beyond the number of change-able characters
                count[s[l]] -= 1
                l+=1 # shrinks the windwo

            maxSize = max(maxSize, r-l+1) #
            r += 1

        return maxSize